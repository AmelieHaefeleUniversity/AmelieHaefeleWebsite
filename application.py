from flask import Flask, render_template

application = app = Flask(__name__)


# https://stackoverflow.com/questions/43728500/python-flask-e-mail-form-example

@app.route("/")
def home():
    return app.send_static_file("index.html")


# @app.route('/user/<name>')
# def user(name):
# return '<h1>Hello %s!!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
