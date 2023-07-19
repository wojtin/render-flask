from flask import Flask, request, jsonify render_template
from PIL import Image
import base64

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/processing', methods=['POST'])
def process():
    file = request.files['image']
    
    img = Image.open(file.stream)
    
    data = file.stream.read()
    #data = base64.encodebytes(data)
    data = base64.b64encode(data).decode()   

    return jsonify({
                'msg': 'success', 
                'size': [img.width, img.height], 
                'format': img.format,
                'img': data
           })
    
if __name__ == '__main__':
    app.run(debug=True)
