from flask import render_template, request, redirect, url_for
from myapp import app, db
from myapp.models import Data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        data = Data(content=content)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('index'))
    data = Data.query.all()
    return render_template('index.html', data=data)

@app.route('/data/<int:id>')
def data(id):
    data = Data.query.get_or_404(id)
    return render_template('data.html', data=data) 