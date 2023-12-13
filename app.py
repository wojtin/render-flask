from flask import Flask, jsonify
from kaggle.api.kaggle_api_extended import KaggleApi
import subprocess

app = Flask(__name__)

@app.route('/')
def fetch_kaggle_dataset():
    # Replace 'your_username' and 'your_kernel_slug' with the actual values
    kernel_slug = 'wojtin/test-print'

    # Set the path to your Kaggle API key file
    api_key_path = 'kaggle.json'

    # Authenticate with Kaggle API
    api = KaggleApi()
    api.authenticate()

    try:
        # Use subprocess to execute the Kaggle command
        subprocess.run(['kaggle', 'kernels', 'push', '-p', '/'])
        return jsonify({'status': 'success', 'message': 'Kaggle kernel pushed successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error pushing Kaggle kernel: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
