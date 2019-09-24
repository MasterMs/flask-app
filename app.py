from flask import Flask, render_template

app = Flask(__name__)

#Routing 
@app.route("/")
def index():
    return render_template('index.html',title='Land',name='Marco')

@app.route("/home")
def home():
    return render_template('index.html', title='Home', name='Home')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

