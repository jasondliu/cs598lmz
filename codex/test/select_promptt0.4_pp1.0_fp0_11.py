import select
# Test select.select() for reading and writing simultaneously

import socket, select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(5)

conn, addr = s.accept()
