# One Piece Image Classifier Web App

## Overview

This web application is a One Piece image classifier built with Python and Flask. It allows users to upload images and get predictions about which One Piece character is depicted. The app utilizes a deep learning model fine-tuned on a pre-trained ResNet34 and exported as an ONNX model. The model is optimized for use with ONNX Runtime and Torch, providing fast and accurate predictions.

## Features

- **Image Upload**: Upload an image of a One Piece character.
- **Prediction**: Get predictions on the character in the image along with probability scores.
- **Clear**: Clear the uploaded image and predictions.
- **Responsive Design**: Works well on both desktop and mobile devices.

## Supported Characters

The model can classify the following One Piece characters:

- Brook
- Chopper
- Franky
- Jinbei
- Luffy
- Nami
- Robin
- Sanji
- Usopp
- Zoro

## Installation

### Prerequisites

- Python 3.8 or higher
- Flask
- ONNX Runtime
- Torch
- TorchVision

### Setup

1. **Clone the Repository**

    ```sh
    git clone https://github.com/mtk3281/One_Piece_Image_Classifier-web-app.git
    ```

2. **Create and Activate a Virtual Environment**

    ```sh
    python -m venv myenv
    ```

    **Activate the virtual environment:**

    - On Windows:

        ```sh
        myenv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source myenv/bin/activate
        ```

3. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Download the Pre-trained Model**

    Ensure that the `op_95%acc.onnx` file is in the project directory. This model has been fine-tuned on a pre-trained ResNet34 using a dataset of One Piece characters and achieves 95% accuracy.

5. **Run the Application**

    ```sh
    python app.py
    ```

    The app will be available at `http://127.0.0.1:5000/`.

## Docker Setup

### Building and Running with Docker

To run the application in a Docker container, follow these steps:

1. **Build the Docker Image**

    ```sh
    docker build -t onepiece-image-classifier .
    ```

2. **Run the Docker Container**

    ```sh
    docker run -p 5000:5000 onepiece-image-classifier
    ```

3. **Access the Application**

    Open your browser and navigate to `http://localhost:5000`.

### Dockerfile Explanation

The Dockerfile is designed to create a lightweight image by utilizing Python Slim and multi-stage builds. It includes only the necessary libraries such as Flask, ONNX Runtime, Torch, and TorchVision to keep the image size small while ensuring that the app runs efficiently.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. For significant changes, please open an issue first to discuss what you would like to change.
