import select
# Test select.select()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 0))
s.listen(1)

conn, addr = s.accept()

print 'Connected by', addr

while 1:
    ready = select.select([conn], [], [], 1)
    if ready[0]:
        data = conn.recv(1024)
        if not data: break
        print data
    else:
        print 'no data'

conn.close()
