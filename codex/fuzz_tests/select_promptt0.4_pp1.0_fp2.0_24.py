import select
# Test select.select()

import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(5)

print 'listening'

inputs = [s]
outputs = []

while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for r in readable:
        if r is s:
            connection, client_address = s.accept()
            print 'new connection from', client_address
            inputs.append(connection)
        else:
            data = r.recv(1024)
            if data:
                print 'got data from', r.getpeername()
                print 'data:', data
                r.send('thanks\n')
            else:
                print 'disconnecting', r.getpeername()
                inputs.remove(r)
                r.close()
    for w in writable:
        print 'writable', w.getpeername()
    for e in exceptional:
        print 'exceptional', e.getpeername()
        inputs.remove(e)
