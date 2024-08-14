One Piece Image Classifier Web App
Overview
This web application is a One Piece image classifier built with Python and Flask. It allows users to upload images and get predictions about which One Piece character is depicted. The app utilizes a deep learning model trained with FastAI and offers a user-friendly interface for image upload and prediction results.

Features
Image Upload: Upload an image of a One Piece character.
Prediction: Get predictions on the character in the image along with probability scores.
Clear: Clear the uploaded image and predictions.
Responsive Design: Works well on both desktop and mobile devices.
Installation
Prerequisites
Python 3.8 or higher
Flask
FastAI
Other required Python packages (listed in requirements.txt)
Setup
Clone the Repository

sh
Copy code
git clone https://github.com/yourusername/One_Piece_Image_Classifier-web-app.git
cd One_Piece_Image_Classifier-web-app
Create and Activate a Virtual Environment

sh
Copy code
python -m venv myenv
Activate the virtual environment:

On Windows:

sh
Copy code
myenv\Scripts\activate
On macOS/Linux:

sh
Copy code
source myenv/bin/activate
Install Dependencies

sh
Copy code
pip install -r requirements.txt
Download the Pre-trained Model

Ensure that the op_95%acc.pkl file is in the project directory.

Run the Application

sh
Copy code
python app.py
The app will be available at http://127.0.0.1:5000/.
