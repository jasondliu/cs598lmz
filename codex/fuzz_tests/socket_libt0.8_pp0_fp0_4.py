import socket
import traceback

from app.utils.logger import Logger


class SmtpClient:
    def __init__(self, server, port, login, password):
        self.logger = Logger(__name__)

        self.server = server
        self.port = port
        self.login = login
        self.password = password

        self.logger.log(f'server: {server} port: {port} login: {login}')

        try:
            self.client = smtplib.SMTP(server, port)
            self.client.ehlo()
            self.client.starttls()
            self.client.login(login, password)
        except Exception as err:
            self.logger.log(f'Init error: {err}')
            traceback.print_exc()

    def send_email(self, to_address, subject, body):
        msg = MIMEText(body, 'html')
        msg['Subject'] = subject
        msg['From'] = self.login
        msg['To'] = to_address
