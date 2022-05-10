import select
# Test select.select()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.python.org', 80))
s.send(b'GET / HTTP/1.0\n\n')

while True:
    readable, writable, exceptional = select.select([s], [], [])
    if readable:
        print(readable)
        print(readable[0].recv(1024))
        break

s.close()
