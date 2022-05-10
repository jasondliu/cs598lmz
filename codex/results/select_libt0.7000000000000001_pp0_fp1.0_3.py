import selectors
import socket
import json
import time
import datetime
import hashlib
import os
import threading

from pynput import mouse, keyboard
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def send_all(sock, data):
	bytes_sent = 0
	while True:
		bytes_sent = bytes_sent + sock.send(data[bytes_sent:])
		if bytes_sent == len(data):
			break

def send(sock, data):
	sock.send(data)

def recv_all(sock, buf_size=4096):
	buffer = bytearray()
	done = False
	while not done:
		part = sock.recv(buf_size)
		if (part):
			buffer.extend(part)
		else:

