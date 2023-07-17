from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Specify the folder to store uploaded images

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image found'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    # Save the uploaded image to the designated folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    # Return the URL of the uploaded image
    return jsonify({'url': f'/uploads/{file.filename}'}), 200

if __name__ == '__main__':
    app.run()
