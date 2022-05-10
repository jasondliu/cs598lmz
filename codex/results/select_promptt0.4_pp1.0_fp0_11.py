import select
# Test select.select() for reading and writing simultaneously

import socket, select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(5)

conn, addr = s.accept()
print 'Connected by', addr

while 1:
    r, w, e = select.select([conn], [conn], [])
    if conn in r:
        data = conn.recv(1024)
        if not data: break
        print 'Received', repr(data)
    if conn in w:
        conn.send('ACK')

conn.close()
