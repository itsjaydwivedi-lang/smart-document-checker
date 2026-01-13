from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MAX_FILE_SIZE_MB = 2
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        report = []

        file = request.files.get('documents')

        if not file or file.filename == '':
            report.append("No file selected")
        else:
            filename = secure_filename(file.filename)

            if not allowed_file(filename):
                report.append("Invalid file format")
            else:
                file.seek(0, os.SEEK_END)
                size_mb = file.tell() / (1024 * 1024)
                file.seek(0)

                if size_mb > MAX_FILE_SIZE_MB:
                    report.append("File size exceeds 2 MB")
                else:
                    file.save(os.path.join(UPLOAD_FOLDER, filename))
                    report.append("File uploaded successfully")
                    report.append("Document meets submission requirements")

        return render_template('result.html', report=report)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


