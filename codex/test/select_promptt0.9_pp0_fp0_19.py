import select
# Test select.select in python
# https://docs.python.org/2/library/select.html

import sys, time
from socket import *

timeout = 5
host = 'localhost'
port = 50008

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host, port))

