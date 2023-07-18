from flask import Flask
import SimpleITK as sitk
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(sitk.Version())
    return 'sj'
