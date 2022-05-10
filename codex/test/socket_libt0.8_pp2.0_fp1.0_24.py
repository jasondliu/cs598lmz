import socket
import twilio
from twilio.rest import TwilioRestClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import system
kernel=str(platform.system())
def config_number(number):
    ACCOUNT_SID = ''
    AUTH_TOKEN = ''
    TWILIO_NUMBER = ''      # +1XXXXXXXXXX
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(to=number, from_=TWILIO_NUMBER,body="Done! You will get email notification when system comes online.")
    return;
def config_email(email):
    msg = MIMEMultipart()
    msg["From"] = ''
    msg["To"] = email
    msg["Subject"] = ""
    body = "Done! You will get email notification when system comes online."
    msg.attach(MIMEText(body, 'plain'))
    server = smt
