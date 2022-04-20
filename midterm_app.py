from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def new_user():
    return render_template("registration.html")



if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)

