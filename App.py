from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Website"

@app.route('/contact')
def contact():
    return "Contact Page"

@app.route('/home')
def home():
    return "Home Page"

@app.route('/gallery')
def gallery():
    return "Gallery Page"

if __name__ == "__main__":
    app.run()
