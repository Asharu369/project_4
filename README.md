### Galaxy Canvas 🌌
Galaxy Canvas is an interactive web app designed for generating and colorizing galaxy images. It utilizes state-of-the-art deep learning techniques, including GANs and U-Nets, to create realistic galaxies and bring black-and-white galaxy images to life. This project leverages WGAN-GP for galaxy generation and Pix2Pix for galaxy colorization.

#### Click Here to see the demonstration of Galaxy Canvas

---

### 🚀 Key Features
1. **Galaxy Generator**: Uses a WGAN-GP model to generate realistic galaxy images from random noise.
2. **Galaxy Colorizer**: Transforms grayscale galaxy images into colorized versions using a U-Net model trained on galaxy data.
3. **Image Saving**: Automatically saves generated galaxies and processed images for future reference.
4. **Interactive Web App**: Built using Streamlit, allowing easy interaction for generating and colorizing images.
5. **API Support**: The backend is powered by FastAPI, providing endpoints for galaxy generation and image colorization.

---

### ⚙️ Setup and Installation
Follow these steps to set up the project locally:

#### Clone the Repository
```bash
git clone https://github.com/Asharu369/project_4.git
```

#### Create a Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Run the API
Start the FastAPI backend for predictions:
```bash
uvicorn main:app --reload
```
Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

#### Visualize Results
Optionally, use Streamlit to interact with the Galaxy Generator and Colorizer:
```bash
streamlit run frontend
```

---

### 🛠️ Training Details

#### Dataset
The model was trained on Galaxy Zoo dataset images, which were preprocessed and augmented. The dataset includes galaxies, stars, and quasars, with labeled data for various tasks like image colorization and classification.

#### Model Architecture
1. **WGAN-GP**: A type of Generative Adversarial Network used to generate galaxy images.
2. **Pix2Pix U-Net**: A U-Net model for image-to-image translation, used here for coloring grayscale galaxy images.
3. **Optimizer**: Adam optimizer with learning rate scheduling.
4. **Loss Function**: Mean Squared Error (MSE) for WGAN-GP and a combination of L1 loss and adversarial loss for Pix2Pix.

#### Training Pipeline
- **Preprocessing**:
  - Images were resized, normalized, and augmented.
  - Grayscale galaxy images were used for colorization.
- **Callbacks**:
  - Model checkpointing to save the best model.
  - Early stopping to prevent overfitting.
- **Metrics**:
  - PSNR (Peak Signal-to-Noise Ratio) for image quality evaluation.

---

### 🌐 API Endpoints

#### Root Endpoint
- **GET /**
  - Returns a JSON response to verify the server status.

#### Generate Galaxy Image
- **POST /generate/**
  - Accepts random noise input and generates a new galaxy image.

#### Colorize Image
- **POST /colorize/**
  - Accepts a grayscale galaxy image and returns the colorized version.

---

### 📚 Acknowledgments
- **TensorFlow/Keras**: For building and training the GAN and U-Net models.
- **FastAPI**: For creating an interactive backend API.
- **Streamlit**: For building the intuitive frontend for user interaction.
- **WGAN-GP**: For generating realistic galaxy images.
- **Pix2Pix**: For colorizing grayscale galaxy images.

