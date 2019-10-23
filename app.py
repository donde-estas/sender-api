from flask import Flask, request
from os import getenv


from flask_mail import Mail, Message

app = Flask(__name__)

# Port es 465 para SSL y 587 para TSL

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=getenv("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER=getenv("MAIL_USERNAME")
    )

mail = Mail(app)

@app.route('/')
def index():
    return "Sender API for Dónde Estás"

@app.route('/send', methods=["GET"])
def sendMail():
    print(request.headers)
    key = request.args.get('key')
    if (key == getenv("KEY")):
        email = request.args.get('email')
        body = request.args.get('body')

        msg = Message("Hello", recipients=[email])
        msg.body = body
        mail.send(msg)
        print(f"Sending to {email}...")
        return f"Sending to {email}..."
    print("Invalid api key")
    return "Invalid api key"

@app.route('/send', methods=["POST"])
def sendMailPost():
    print(request.headers)
    key = request.args.get('key')
    if (key == getenv("KEY")):
        email = request.args.get('email')
        body = request.args.get('body')

        msg = Message("Hello", recipients=[email])
        msg.body = body
        mail.send(msg)
        print(f"Sending to {email}...")
    print("Invalid api key")


