from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Initialize the Flask application
app = Flask(__name__)

# Load the PKL model
pkl_model_path = 'C:\\Users\\RIJUL GULATI\\Documents\\Custom Office Templates\\OneDrive\\Desktop\\MINI PROJECT\\random_forest_model.pkl'
pkl_model = joblib.load(pkl_model_path)

# Load the CNN model
model_path = 'C:\\Users\\RIJUL GULATI\\Documents\\Custom Office Templates\\OneDrive\\Desktop\\MINI PROJECT\\xception.keras'
model = load_model(model_path)

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Label mappings for Keras model
LABELS_CNN = {
    0: "Normal",
    1: "RPM Spoofing",
    2: "Gear Spoofing",
    3: "DoS attack",
    4: "Fuzzy Attack"
}

# Label mappings for PKL model
LABELS_PKL = {
    0: "DoS Attack",
    1: "Fuzzy Attack",
    2: "Normal",
    3: "RPM Spoofing",
    4: "Gear Spoofing"
}

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to render the main page
@app.route('/')
def index():
    return render_template('app.html')

# Route for PKL model prediction with 9 direct inputs
@app.route('/predict_data', methods=['POST'])
def predict_data():
    try:
        # Get 9 inputs directly from form data
        input_data = [float(request.form[f'input{i+1}']) for i in range(9)]
        
        # Convert input data to numpy array and reshape for prediction
        input_data = np.array(input_data).reshape(1, -1)
        prediction_index = pkl_model.predict(input_data)[0]

        # Get the corresponding label for the PKL model
        label = LABELS_PKL.get(prediction_index, "Unknown")

        return jsonify({"prediction": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route for Keras model prediction with image input
@app.route('/predict_image', methods=['POST'])
def predict_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        try:
            # Load the image using PIL directly from the file stream
            img = Image.open(file.stream)
            img = img.resize((224, 224))  # Resize to the input size expected by your model
            img_array = img_to_array(img) / 255.0  # Normalize to [0, 1]
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

            # Predict using the Keras model
            prediction = model.predict(img_array)
            label_index = np.argmax(prediction)

            # Get the corresponding label for the CNN model
            label = LABELS_CNN.get(label_index, "Unknown")  # Fallback to "Unknown" if index not in LABELS_CNN

            return jsonify({"prediction": label})
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return jsonify({"error": f"Prediction failed: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid file type"}), 400

# Run the server
if __name__ == '__main__':
    app.run(debug=True)