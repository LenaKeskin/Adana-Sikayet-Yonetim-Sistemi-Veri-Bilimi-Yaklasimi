from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        df = pd.read_csv(filepath)
        mean_values = df.describe().loc['mean'].to_dict()

        # Grafik kaydet (örnek)
        if not os.path.exists('static'):
            os.makedirs('static')
        plt.figure(figsize=(10,5))
        df.select_dtypes(include='number').hist(bins=20)
        plt.tight_layout()
        plt.savefig('static/histogram.png')
        plt.close()

        return render_template('result.html', mean_values=mean_values)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return "Dosya yüklenmedi", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)
    mean_values = df.describe().loc['mean'].to_dict()

    # Grafik kaydet
    if not os.path.exists('static'):
        os.makedirs('static')
    plt.figure(figsize=(10,5))
    df.select_dtypes(include='number').hist(bins=20)
    plt.tight_layout()
    plt.savefig('static/histogram.png')
    plt.close()

    return render_template('result.html', mean_values=mean_values)

# ---- Web API endpoint ----
@app.route('/api/upload', methods=['POST'])
def api_upload():
    if 'file' not in request.files:
        return jsonify({"error": "Dosya bulunamadı"}), 400

    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)
    mean_values = df.describe().loc['mean'].to_dict()

    return jsonify({"mean_values": mean_values})

if __name__ == '__main__':
    app.run(debug=True)
