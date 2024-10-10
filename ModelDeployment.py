from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model (make sure to replace with your model's path)
try:
    with open('ridge_model.pkl', 'rb') as model_file:  # Use joblib if you saved with it
        model = joblib.load(model_file)
    print("Model loaded successfully:", type(model))
except Exception as e:
    print("Error loading model:", e)
    model = None  # Set model to None if loading fails


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Ensure that 'features' is in the input data
    if 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400

    features = data['features']

    # Print the received features for debugging
    print("Received features:", features)
    print("Type of features:", type(features))
    print("Length of features:", len(features))

    # Make sure the input features are in the correct shape
    if len(features) != 14:  # Replace with the actual number of features
        return jsonify({'error': 'Invalid number of features'}), 400

    # Ensure that model is loaded
    if model is None or not hasattr(model, 'predict'):
        return jsonify({'error': 'Model not loaded correctly'}), 500

    try:
        prediction = model.predict([features])  # Predict price
        return jsonify({'price': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
