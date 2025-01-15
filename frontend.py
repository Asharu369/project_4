import streamlit as st
import base64
import requests
from PIL import Image
import io
import os
from backend import RGB_DIR, GALAXY_DIR

# API endpoints
GENERATE_API = "http://localhost:8000/generate/"
COLORIZE_API = "http://localhost:8000/colorize/"

# Constants for background images
BACKGROUND_IMAGES = {
    "Information Page": "background_images/static_image.jpg",
    "Galaxy Generator Page": "background_images/galaxy_generator.jpg",
    "Galaxy Colorizer Page Initial": "background_images/galaxy_coloriser.JPG",
    "Galaxy Colorizer Page After": "background_images/after.jpg",
}

# Set up the Streamlit page layout
st.set_page_config(page_title="Galaxy Canvas", layout="wide", page_icon="🌌")

# Function to apply a dynamic background image
def apply_background(image_path):
    try:
        with open(image_path, "rb") as f:
            img_data = f.read()
        encoded_img = base64.b64encode(img_data).decode("utf-8")
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_img}");
                background-size: cover;
            }}
            .transparent-box {{
                background: rgba(0, 0, 0, 0.7);
                color: white;
                padding: 20px;
                border-radius: 10px;
            }}
            .sidebar .css-1d391kg {{
                background: rgba(0, 0, 0, 0.8) !important;
                color: white;
                border-radius: 15px;
            }}
            .sidebar .css-1d391kg h2 {{
                color: white;
                font-weight: bold;
            }}
            .css-18ni7ap .stRadio > label {{
                background: rgba(0, 0, 0, 0.8);
                color: white;
                border-radius: 5px;
                padding: 5px 10px;
            }}
            .css-18ni7ap .stRadio > div[data-baseweb="radio"] > label {{
                color: white;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    except FileNotFoundError:
        st.error(f"Background image not found: {image_path}")

# Sidebar navigation with transparent black styling
st.sidebar.markdown(
    """
    <div style="background: rgba(0, 0, 0, 0.8); padding: 15px; border-radius: 10px;">
        <h2>Galaxy Canvas</h2>
        <p>Navigate through the app using the menu below:</p>
    </div>
    """,
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "Navigate to:", ["Information Page", "Galaxy Generator Page", "Galaxy Colorizer Page"]
)

# Initialize session state for 'uploaded' and 'colorized' if not present
if "uploaded" not in st.session_state:
    st.session_state.uploaded = False
if "colorized" not in st.session_state:
    st.session_state.colorized = False

# Render pages based on navigation
if page == "Information Page":
    apply_background(BACKGROUND_IMAGES["Information Page"])

    # Tabs for sections
    tab1, tab2, tab3 = st.tabs(["🌟 Overview", "📚 How to Use", "🧠 AI Models"])

    with tab1:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown(
                """
                <div style="background: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 10px;">
                <h1 style="color: #FFD700;">✨ Welcome to Galaxy Canvas ✨</h1>
                <p style="color: white;">Galaxy Canvas is an AI-powered app designed to create and colorize stunning galaxy images. Whether you're a space enthusiast or looking for some cosmic fun, this app is a must-try for you!</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                """
                <div style="background: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 10px;">
                <p style="color: white;">Generated images are stored in your local system. This project is developed by Muhammed Asharudheen as part of the ML4A Training Program at Spartifical.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with tab2:
        st.markdown(
            """
            <div class="transparent-box">
            <h3 style="color: #FFD700;">📚 How to Use</h3>
            <ul>
                <li><b>Galaxy Generator:</b> Create breathtaking galaxy images with a single click.</li>
                <li><b>Galaxy Colorizer:</b> Upload a grayscale galaxy image and watch AI bring it to life with colors.</li>
            </ul>
            <h4>Instructions:</h4>
            <ol>
                <li>Use the navigation menu to explore different features.</li>
                <li>Read the feature descriptions and follow the steps provided.</li>
                <li>Enjoy the cosmic journey!</li>
            </ol>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab3:
        st.markdown(
            """
            <div class="transparent-box">
            <h3 style="color: #FFD700;">🧠 AI Models in Use</h3>
            <h4 style="color: #FFD700;">WGAN-GP (Wasserstein Generative Adversarial Network - Gradient Penalty)</h4>
            <ul>
                <li><b>Purpose:</b> Generates high-quality, realistic galaxy images.</li>
                <li><b>How It Works:</b>
                    <ul>
                        <li>Uses a critic network instead of a discriminator for better training stability.</li>
                        <li>Employs the Wasserstein distance to measure how realistic the generated galaxies are.</li>
                        <li>Implements a gradient penalty to enforce smoothness and avoid mode collapse.</li>
                    </ul>
                </li>
            </ul>
            <h4 style="color: #FFD700;">Pix2Pix (Image-to-Image Translation GAN)</h4>
            <ul>
                <li><b>Purpose:</b> Adds realistic colors to grayscale galaxy images.</li>
                <li><b>How It Works:</b>
                    <ul>
                        <li>Uses paired training data to learn a mapping from grayscale to color images.</li>
                        <li>Employs a generator to produce colorized images and a discriminator to critique their realism.</li>
                    </ul>
                </li>
            </ul>
            <h4 style="color: #FFD700;">Tools Used:</h4>
            <ul>
                <li><b>TensorFlow & Keras:</b> Training of Galaxy Generator using Wasserstein GAN.</li>
                <li><b>PyTorch:</b> Training of Galaxy Colorizer using Pix2Pix GAN.</li>
                <li><b>FastAPI:</b> Backend development.</li>
                <li><b>Streamlit:</b> Frontend development.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif page == "Galaxy Generator Page":
    apply_background(BACKGROUND_IMAGES["Galaxy Generator Page"])
    st.markdown(
        """
        <div class="transparent-box">
        <h1>Galaxy Generator</h1>
        <p>Click the button below to generate a new galaxy image!</p>
        <h3>Instructions:</h3>
        <ol>
            <li>Click the "Generate Galaxy" button.</li>
            <li>Wait for the AI to create your galaxy.</li>
            <li>View and save the generated image.</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Generate Galaxy"):
        with st.spinner("Generating your galaxy..."):
            response = requests.post(GENERATE_API)
            if response.status_code == 200:
                latest_image = sorted(os.listdir(GALAXY_DIR))[-1]
                image_path = os.path.join(GALAXY_DIR, latest_image)
                image = Image.open(image_path).convert("L")
                st.image(image, caption="Generated Grayscale Galaxy")
            else:
                st.error("Failed to generate galaxy. Please try again.")

elif page == "Galaxy Colorizer Page":
    # Determine the background dynamically
    if st.session_state.colorized:
        apply_background(BACKGROUND_IMAGES["Galaxy Colorizer Page After"])
    else:
        apply_background(BACKGROUND_IMAGES["Galaxy Colorizer Page Initial"])

    st.markdown(
        """
        <div class="transparent-box">
        <h1>Galaxy Colorizer</h1>
        <p>Upload a grayscale galaxy image to colorize it.</p>
        <h3>Instructions:</h3>
        <ol>
            <li>Click "Upload Image" to upload a grayscale galaxy image.</li>
            <li>Wait for the AI to colorize your image.</li>
            <li>View the original and colorized images.</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.session_state.uploaded = True
        image = Image.open(uploaded_file)
        grayscale_image = image.convert("L")

        with st.spinner("Colorizing your galaxy..."):
            img_byte_arr = io.BytesIO()
            grayscale_image.save(img_byte_arr, format="PNG")
            img_byte_arr.seek(0)
            files = {"file": img_byte_arr.getvalue()}

            response = requests.post(COLORIZE_API, files=files)
            if response.status_code == 200:
                st.session_state.colorized = True
                apply_background(BACKGROUND_IMAGES["Galaxy Colorizer Page After"])
                latest_image = sorted(os.listdir(RGB_DIR))[-1]
                image_path = os.path.join(RGB_DIR, latest_image)

                col1, col2 = st.columns(2)
                with col1:
                    st.image(grayscale_image, caption="Uploaded Grayscale Image", use_column_width=True)
                with col2:
                    st.image(image_path, caption="Colorized Galaxy", use_column_width=True)
            else:
                st.error("Failed to colorize galaxy. Please try again.")
