import select
# Test select.select()

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))
sock.setblocking(0)

while True:
    try:
        data = sock.recv(1024)
        print data
    except socket.error:
        pass
    r, w, e = select.select([sock], [], [], 0.1)
    if sock in r:
        data = sock.recv(1024)
        print data
    else:
        print 'no data'
