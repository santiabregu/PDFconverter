from flask import Flask, request, send_file
from pdf2image import convert_from_path
import io
import os

upload_folder = 'uploads'
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app = Flask(__name__)

# Configure PDF2Image
app.config['UPLOAD_FOLDER'] = 'uploads'

"""
@app.route('/convert_pdf_to_image', methods=['POST'])
def convert_pdf_to_image():
    # Get PDF file from POST request
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file', 400
    
    # Save the uploaded PDF file temporarily
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(pdf_path)
    
    try:
        images = convert_from_path(pdf_path, first_page=1, last_page=1)  # You can convert all pages if needed
        image = images[0]
        
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    
    except Exception as e:
        return str(e), 500
    """

@app.route('/convert_pdf_to_image', methods=['POST'])
def convert_pdf_to_image():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file', 400
    
    # Save the uploaded PDF file temporarily
    pdf_path = os.path.join('uploads', file.filename)
    file.save(pdf_path)

    try:
        # Ensure Poppler is correctly specified
        images = convert_from_path(pdf_path, poppler_path=r'C:\Program Files\poppler-24.08.0\Library\bin')
        
        # Save the first image to a BytesIO object and return it
        img_io = io.BytesIO()
        images[0].save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
