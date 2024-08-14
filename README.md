# One Piece Image Classifier Web App

## Overview

This web application is a One Piece image classifier built with Python and Flask. It allows users to upload images and get predictions about which One Piece character is depicted. The app utilizes a deep learning model trained with FastAI and offers a user-friendly interface for image upload and prediction results.

## Features

- **Image Upload**: Upload an image of a One Piece character.
- **Prediction**: Get predictions on the character in the image along with probability scores.
- **Clear**: Clear the uploaded image and predictions.
- **Responsive Design**: Works well on both desktop and mobile devices.

## Installation

### Prerequisites

- Python 3.8 or higher
- Flask
- FastAI
- Other required Python packages (listed in `requirements.txt`)

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

   Ensure that the `op_95%acc.pkl` file is in the project directory.

5. **Run the Application**

    ```sh
    python app.py
    ```

    The app will be available at `http://127.0.0.1:5000/`.


