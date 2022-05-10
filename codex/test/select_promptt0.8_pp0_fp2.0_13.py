import select
# Test select.select function
# https://docs.python.org/3.5/library/select.html

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

