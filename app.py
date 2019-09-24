from flask import Flask
app = Flask(__name__)

def readAssign(file):
    file = open('index.html', 'r')
    index = file.read()
    file.close()
    return index


@app.route("/")
def hello():
    return readAssign(file='index.html')