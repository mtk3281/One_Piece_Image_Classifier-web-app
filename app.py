from flask import Flask, request, render_template, redirect, url_for
from fastai.vision.all import load_learner, PILImage
import os
import pathlib

app = Flask(__name__)

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


# Load the FastAI model
model_path = 'op_95%acc.pkl'
learn = load_learner(model_path)

# Ensure the 'static' folder exists
os.makedirs('static', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file:
            try:
                print(f"Received file: {file.filename}")
                
                # Save the uploaded file to the static folder
                file_path = os.path.join('static', file.filename)
                file.save(file_path)
                
                # Create a PIL image using the saved file path
                img = PILImage.create(file_path)
                
                # Make predictions
                pred, pred_idx, probs = learn.predict(img)
                
                # Convert probabilities to a list of floats
                probs = probs.tolist()
                
                # Get top 3 predictions
                top_probs, top_labels = zip(*sorted(zip(probs, learn.dls.vocab), reverse=True)[:3])
                top_probs = [f'{p:.2f}' for p in top_probs]

                return render_template('index.html', 
                                       image=file.filename,
                                       predictions=zip(top_labels, top_probs),
                                       predicted_label=pred,
                                       predicted_prob=max(probs))
            except Exception as e:
                print(f"Error processing image: {e}")
                return render_template('index.html', predictions=None, error="Failed to process image. Please try again with a different image.")

    return render_template('index.html', predictions=None)


@app.route('/clear')
def clear():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
