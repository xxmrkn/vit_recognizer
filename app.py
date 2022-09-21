from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    fuga = '123'
    return render_template("index.html", hoge=fuga)

@app.route('/upload', methods=['post'])
def upload():
    img_file = request.files['img_file']
    print(img_file.filename)
    filename = secure_filename(img_file.filename)
    print(filename)
    ul_path = f'./static/{filename}'
    img_file.save(ul_path)
    return render_template('index.html', img_url=ul_path)

@app.route('/recognition', methods=['post'])
def recognition():
    img_path = request.form['img_path']
    print(img_path)
    return render_template('index.html', img_url=img_path)

if __name__ == "__main__":
    app.run(debug=True)
