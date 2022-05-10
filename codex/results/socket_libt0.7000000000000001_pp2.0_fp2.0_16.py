import socket
import ssl
import threading
import time
import _thread
import sys
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

from struct import pack

from core import *
from getMail import *
from mail import *

threads = []

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('0.0.0.0', 465)

print('Starting up on %s port %s' % server_address)

s.bind(server_address)

s.listen(5)

def sendMail(from_addr, to_addr, subject, body,
