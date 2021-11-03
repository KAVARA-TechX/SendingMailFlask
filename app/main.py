from flask import Flask

import smtplib



app = Flask(__name__)

@app.route("/")
def index():
    s = smtplib.SMTP('smtp.gmail.com','587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("kavara.tracker@gmail.com", "Kavara@123")
    SUBJECT="Sending mail"
    TEXT="Hello"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("kavara.tracker@gmail.com", "ka340689@gmail.com",message )
    s.quit()
    return "Sent"

