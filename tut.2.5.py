from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    content = "hello, world!"
    numbers = list(range(10))
    return render_template("index.html", content=content, numbers=numbers)


if __name__ == '__main__':
    app.run(debug=True)