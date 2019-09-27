from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


#Routing 
@app.route("/")
def index():
    return render_template('index.html',title='Landing',name='Landing')

@app.route("/home")
def home():
    return render_template('index.html', title='Home', name='Home')

@app.route('/help')
def help():
    return render_template('index.html', title='Help', name='Help')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == "__main__":
    app.run()

