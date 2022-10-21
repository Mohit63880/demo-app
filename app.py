from flask import Flask

app = Flask(__name__)

@app.route('/api/customer')
def customers():
    pass

@app.route('/')
def index():
    return "<h1>Hello World</h1>"