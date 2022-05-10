import selectors
import socket
import sys
import types
import time
import threading
import os
import datetime
import random

from Crypto.Cipher import AES
from Crypto.Util import Counter

import rsa
import rsa_util
import util

import logging
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------
#
# ---------------------------------------------------------------------

def get_server_key(server_ip):
    return rsa_util.get_public_key(server_ip)

# ---------------------------------------------------------------------
#
# ---------------------------------------------------------------------

class Client:

    def __init__(self, server_ip, server_port, username, password):
        self.server_ip = server_ip
        self.server_port = server_port
        self.username = username
        self.password = password
        self.server_key = get_server_key(server_ip)
        self.client_key = rsa_util.get_private_key()

        self.sel = selectors.DefaultSelector()

    def start(self):
        self.start_connection
