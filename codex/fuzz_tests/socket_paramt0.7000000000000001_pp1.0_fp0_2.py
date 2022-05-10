import socket
socket.if_indextoname('1')

import subprocess
subprocess.run(['ping', '-c', '3', 'www.google.com'])

import sys
sys.stdin.fileno()

import tempfile
tempfile.TemporaryFile().fileno()

import test
test.get_original_stdin()

import threading
threading.current_thread()

import time
time.time()

import urllib
urllib.request.urlopen('https://www.google.com')

import xmlrpc
xmlrpc.client
