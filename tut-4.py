from typing import Optional
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.2.0.html")
@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', user=user))
    else:
        return render_template("login.html")

@app.route('/user')
def user():
    args_dict: dict = request.args
    user: Optional[str] = args_dict.get('user', 'Default User')
    return f"<h1>{user}</h1>"

if __name__ == '__main__':
    app.run(debug=True)