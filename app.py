from flask import Flask
app = Flask(__name__)

index = open('index.html', 'r')

@app.route("/")
def hello():
    return "Yo Fam"