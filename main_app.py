from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "Welcome to the Printing Shop!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/analyze_pdf', methods=['POST'])
def analyze_pdf():
    data = request.get_json()  # expect JSON data with file name
    file_name = data.get('file_name')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    # Here would be the PDF analysis logic. For now, return file name only.
    return jsonify({'message': f'Analyzing {file_name}'}), 200

@app.route('/calculate_price', methods=['POST'])
def calculate_price():
    data = request.get_json()  # expect JSON data with parameters for pricing
    quantity = data.get('quantity', 1)  # default to 1 if not provided
    price_per_page = 0.10  # example price per page
    total_price = price_per_page * quantity
    return jsonify({'total_price': total_price}), 200

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ensure upload folder exists
    app.run(debug=True)