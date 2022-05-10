import select
# Test select.select()

import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(5)

