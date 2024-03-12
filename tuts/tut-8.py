from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask import flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def home():
    return render_template("index.2.0.html")

@app.route('/view')
def view():
    return render_template("view.html", values=users.query.all())

@app.route('/login',methods=['POST', 'GET'])
def login():
    session.permanent = True
    if request.method == 'POST':
        email= request.form['email']
        session["email"] = email

        found_user = users.query.filter_by(name=user).delete()
        for user in found_user:
            user.delete()
        if found_user:
            session["email"] = found_user.email
            found_user= users.query.filter_by(name=user).first()
            found_user.email = email
        else:
            usrs= users(users,None)
            db.session.add(usrs)
            db.session.commit()
        
        return redirect(url_for, user = user)
    else:
        if 'user' in session:
            flash("Already Logged In!", "info")
            return redirect(url_for('user'))
        
        return render_template("login-2.html")

@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            flash("Email was saved!")
        return render_template("user2.html", email= email)
    else:
        if 'email' in session:
             email = session['email']


        flash("You are not logged in!", "info")
        return redirect(url_for("login"))
    
@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        session.pop('email', None)
        flash("You have been logged out!", "info")
    return redirect(url_for("login"))

if __name__ == '__main__':
    db.create_all
    app.run(debug=True)