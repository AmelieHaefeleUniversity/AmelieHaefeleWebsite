import flask
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from flask_mail import Mail, Message
from flask import send_from_directory

application = app = Flask(__name__, static_folder="static")

app.config.update(dict(
    MAIL_SERVER='smtp.googlemail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='amelieresumewebsite@gmail.com',
    MAIL_PASSWORD='P3n2guin!'
))

mail = Mail(app)


@app.route("/")
def home():
    title = "Home"
    return render_template("index.html", title=title)


@app.route("/download/")
def pdf():
    # return flask.send_from_directory('static/resume.PDF', as_attachment=True)
    return send_from_directory('/static/resume.PDF', attachment_filename='resume.PDF')


@app.route("/contactMe", methods=["GET"])
def contactMe():
    title = "Contact me"
    return render_template("contact.html", title=title)


@app.route("/emailSubmit", methods=["POST"])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    if not name or not email or not message:
        flash = "Name, Email, and Message are required"
        return redirect(url_for('contactMe'))

    msg = Message('Email from {} / {} with subject {}'.format(name, email, subject),
                  sender='amelieresumewebsite@gmail.com', recipients=['amelie@haefele.org'],
                  body="{} {}".format(email, message))
    mail.send(msg)

    return render_template("emailSubmitted.html")


if __name__ == '__main__':
    app.run(debug=True)
