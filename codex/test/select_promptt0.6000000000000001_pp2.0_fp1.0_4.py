import select
# Test select.select() for readability with a timeout.

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(1)
s.setblocking(0)

conn, addr = s.accept()

