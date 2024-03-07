from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder='templates2')

@app.route("/Home2")
@app.route("/")
def home():
    return render_template("home2.html")

if __name__ == "__main__":
    app.run(debug=True)