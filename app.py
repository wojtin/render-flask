from flask import Flask
import SimpleITK as sitk
app = Flask(__name__)

print(sitk.Version())

@app.route('/')
def hello_world():
    return sitk.Version()
