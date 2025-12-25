import smtplib
from email.message import EmailMessage
from email.utils import parseaddr
from config import EMAIL, APP_PASSWORD

def send_reply(to, subject, body):
    real_email = parseaddr(to)[1]   

    msg = EmailMessage()
    msg.set_content(body)
    msg["From"] = EMAIL
    msg["To"] = real_email
    msg["Subject"] = subject

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
