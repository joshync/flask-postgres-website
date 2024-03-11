from flask import Flask,  render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.2.0.html", content="testing")

if __name__ == '__main__':
    app.run(debug=True)