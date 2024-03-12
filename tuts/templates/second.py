import os
from flask import Blueprint, render_template

second= Blueprint('second', __name__, static_folder="static", template_folder=os.path.abspath('templates')) 

@second.route("/home")
@second.route('/')
def home():
    return render_template('home2.html')


templates_auto_reload = True
# Path: templates/home2.html
