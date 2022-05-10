import select
# Test select.select
# test_select.py

import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8001))
sock.listen(5)

inputs = [sock]
outputs = []

while True:
    rs, ws, es = select.select(inputs, outputs, inputs)
    print 'waiting for next event'
    print 'rs: ', rs
    print 'ws: ', ws
    print 'es: ', es
    for r in rs:
        if r is sock:
            conn, addr = sock.accept()
            print 'new connection from ', addr
            inputs.append(conn)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print r.getpeername(), 'disconnected'
                inputs.remove(r)
            else:
                print data
