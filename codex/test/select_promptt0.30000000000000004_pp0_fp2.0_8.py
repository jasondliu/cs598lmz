import select
# Test select.select() with a timeout of 0.0

import select
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 0))
s.listen(1)

r, w, x = select.select([s], [], [], 0.0)
