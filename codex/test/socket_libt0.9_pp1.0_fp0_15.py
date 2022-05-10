import socket
from datetime import datetime


class Email:
    def __init__(self, subject, message):
        self.subject = subject
        self.message = message

