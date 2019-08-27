from flask import Flask
app = Flask(__name__)

f = open('index.html', 'r')
index = f.read()
f.close()


print(index)
@app.route("/")
def hello():
    return index