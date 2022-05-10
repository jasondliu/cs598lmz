import socket
from datetime import datetime


class Email:
    def __init__(self, subject, message):
        self.subject = subject
        self.message = message

    def _sendEmail(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('server.pi.1.1@gmail.com', 'vp9xg6yh')
            msg = MIMEMultipart()
            msg['From'] = 'server.pi.1.1@gmail.com'
            msg['To'] = 'server.pi.1.1@gmail.com'
            msg['Subject'] = self.subject
            msg.attach(MIMEText(self.message, 'plain'))
            server.sendmail('server.pi.1.1@gmail.com', 'server.pi.1.1@gmail.com', msg)
            print("Email notification sent!")
            server.close()

        except
