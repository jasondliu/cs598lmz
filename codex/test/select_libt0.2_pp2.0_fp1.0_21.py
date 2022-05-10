import select
import socket
import sys
import threading
import time

import paramiko
from paramiko.py3compat import u

# setup logging
paramiko.util.log_to_file('demo_server.log')

host_key = paramiko.RSAKey(filename='test_rsa.key')
print('Read key: ' + u(host_key.get_base64()))

class Server (paramiko.ServerInterface):
    def _init_(self):
        self.event = threading.Event()
