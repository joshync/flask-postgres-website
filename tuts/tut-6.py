from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask import flash

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)

@app.route('/')
def home():
    return render_template("index.2.0.html")
@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        flash("Login Successful!", "info")
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash("Already Logged In!", "info")
            return redirect(url_for('user'))
        
        return render_template("login-2.html")

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!", "info")
        return redirect(url_for("login"))
    
@app.route('/logout')
def logout():
    if user in session:
        user = session['user']
        flash("You have been logged out!", "info")
    session.pop('user', None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)