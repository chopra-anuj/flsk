from flask import Flask, render_template
from flask import send_file

app = Flask(__name__)

@app.route("/")
def index():
    return "Hurray!!"

@app.route("/image1/")
def image1():
    return render_template("image1.html")

@app.route("/image2/")
def image2():
    return render_template("image2.html")


if __name__ == '__main__':
    app.run()
