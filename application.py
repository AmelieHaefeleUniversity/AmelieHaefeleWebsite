from flask import Flask
app = Flask(__name__)

# https://stackoverflow.com/questions/43728500/python-flask-e-mail-form-example

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)