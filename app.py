from flask import Flask
import util

app = Flask(__name__)

@app.route("/")
def index():
    return util.readAssign(file='index.html')

if __name__ == "__main__":
    app.run()

