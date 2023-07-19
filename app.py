from flask import Flask, request, jsonify, render_template
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route('/')
def index():
   return '''Server Works6!<hr>
<form action="/processing" method="POST" enctype="multipart/form-data">
<input type="file" name="image">
<button>OK</button>
</form>    '''

@app.route('/processing', methods=['POST'])
def process():
    file = request.files['image']
    
    img = Image.open(file.stream)
    
    image_buffer = io.BytesIO(decoded_image)
    sitk_image = sitk.ReadImage(image_buffer)  

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
    app.run(debug=True)
