from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MAX_FILE_SIZE_MB = 2
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

# ---------------- HELPER ----------------
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------------- INDEX PAGE ----------------
@app.route('/', methods=['GET', 'POST'])
def index():
    report = []

    if request.method == 'POST':
        file = request.files.get('documents')

        if not file or file.filename == '':
            report.append(" No file selected")
        else:
            filename = secure_filename(file.filename)

            if not allowed_file(filename):
                report.append(" Invalid file type")
            else:
                file.seek(0, os.SEEK_END)
                size_mb = file.tell() / (1024 * 1024)
                file.seek(0)

                if size_mb > MAX_FILE_SIZE_MB:
                    report.append(" File size exceeds 2 MB")
                else:
                    file.save(os.path.join(UPLOAD_FOLDER, filename))
                    report.append("✅ File uploaded successfully")
                    report.append("✅ Document is submission-ready")

        return redirect(url_for('result'))

    return render_template('index.html')

# ---------------- RESULT PAGE ----------------
@app.route('/result')
def result():
    return render_template('result.html')

# ---------------- RUN SERVER ----------------
if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)
