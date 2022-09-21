from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    fuga = '123'
    return render_template("index.html", hoge=fuga)

@app.route('/upload')
def upload():
    img_file = request.files['img_file']
    print(img_file.filename)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
