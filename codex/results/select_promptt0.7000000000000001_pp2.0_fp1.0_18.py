import select
# Test select.select

import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 20000))
s.listen(1)

while True:
    conn, addr = s.accept()
    while True:
        try:
            rlist, wlist, xlist = select.select([conn],[],[])
        except:
            print 'except'
            break
        if rlist:
            print 'here'
            data = conn.recv(1024)
            print data
            if not data:
                break
            conn.send(data)
    conn.close()
