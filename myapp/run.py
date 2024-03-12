from myapp import app, db
from myapp.models import Data

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True) 