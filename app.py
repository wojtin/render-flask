from flask import Flask, render_template, request, jsonify
import SimpleITK as sitk
import base64
import io

app = Flask(__name__)

@app.route('/')
def index():
    print(sitk.Version())
    return

@app.route('/convert', methods=['POST', 'OPTIONS'])
def convert_image():
    if request.method == 'OPTIONS':
        # Handle pre-flight request for CORS
        headers = {
            'Access-Control-Allow-Origin': '*',  # Replace '*' with your desired domain
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return ('', 204, headers)

    image_data = request.json['image_data']
    image_data = image_data.split(',')[1]  # Remove the data:image/png;base64 prefix

    # Convert base64 string to image
    decoded_image = base64.b64decode(image_data)
    sitk_image = sitk.ReadImageFromMemory(decoded_image)
    
    # Convert to grayscale
    sitk_image = sitk.RescaleIntensity(sitk_image)
    sitk_image = sitk.Cast(sitk_image, sitk.sitkUInt8)

    # Convert image to base64 string
    output_buffer = io.BytesIO()
    sitk.WriteImage(sitk_image, output_buffer)
    output_buffer.seek(0)
    encoded_image = base64.b64encode(output_buffer.getvalue()).decode('utf-8')

    return jsonify(encoded_image)

if __name__ == '__main__':
    app.run()
