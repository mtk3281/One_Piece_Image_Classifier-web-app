from flask import Flask, request, render_template, redirect, url_for
import os
import onnxruntime as ort
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
import os
import platform
import pathlib
import torch
import torch.nn.functional as F


if platform.system() == 'Windows':
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
else:
    pass

app = Flask(__name__)

model_path = 'op_95%acc.onnx'
labels = ['Brook', 'Chopper', 'Franky', 'Jinbei', 'Luffy', 'Nami', 'Robin', 'Sanji', 'Usopp', 'Zoro']

ort_session = ort.InferenceSession(model_path)


os.makedirs('static', exist_ok=True)


def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img = transform(img).unsqueeze(0)  
    return img.numpy()


def predict(image_path):
    input_data = preprocess_image(image_path)
    ort_inputs = {ort_session.get_inputs()[0].name: input_data}
    ort_outs = ort_session.run(None, ort_inputs)
    
    # print(f"ONNX model output shape: {ort_outs[0].shape}")
    
    probs = F.softmax(torch.tensor(ort_outs[0][0]), dim=0).numpy()
    return probs


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file:
            try:
                print(f"Received file: {file.filename}")

                file_path = os.path.join('static', file.filename)
                file.save(file_path)

                output = predict(file_path)

                top_indices = np.argsort(output)[::-1][:3]
                top_probs = output[top_indices].tolist()
                top_labels = [labels[i] for i in top_indices]

                top_probs = [f'{p:.2f}' for p in top_probs] 

                predicted_label = top_labels[0]
                predicted_prob = float(top_probs[0])

                return render_template('index.html',
                                    image=file.filename,
                                    predictions=zip(top_labels, top_probs),
                                    predicted_label=predicted_label,
                                    predicted_prob=predicted_prob)

            except Exception as e:
                print(f"Error processing image: {e}")
                return render_template('index.html', predictions=None, error="Failed to process image. Please try again with a different image.")

    return render_template('index.html', predictions=None)

@app.route('/clear')
def clear():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
