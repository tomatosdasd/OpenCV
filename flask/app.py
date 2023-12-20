import base64
import os

import numpy as np
import open
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main():
    print()
    return render_template('main.html')

@app.route('/uploader', methods=["POST"])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        file_bytes = f.read()
        img = open.analyze(file_bytes)
        
        return redirect('/')
    # return render_template('main.html', img= base64.b64encode(img).decode('utf-8') )


if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)



