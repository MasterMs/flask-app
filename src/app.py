from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


engine = db.create_engine(f'dialect+driver://root:marco123@localhost:3306/myDB')
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
        return f'<User {self.username}>'



if __name__ == "__main__":
    app.run(host='localhost', port=8080)

