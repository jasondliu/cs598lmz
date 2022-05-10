import socket
import sys
import time
import threading
import os
import signal
import random
import string
import hashlib
import base64
import json
import re
import binascii

def create_nonce(length = 8):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])

def create_hash(nonce, secret):
    return hashlib.sha256(nonce.encode() + secret.encode()).hexdigest()

def create_response(nonce, hash):
    return base64.b64encode(json.dumps({'nonce': nonce, 'hash': hash}).encode()).decode()

def decode_response(response):
    return json.loads(base64.b64decode(response).decode())

def check_response(response, secret):
    data = decode_response(response)
    return data['hash'] == create_hash(data['nonce'], secret)

