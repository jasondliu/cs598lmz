import select
# Test select.select()

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 0))
sock.listen(5)

port = sock.getsockname()[1]

print('listening on port', port)

inputs = [sock]
outputs = []
excepts = []

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, excepts)
    for s in readable:
        if s is sock:
            connection, client_address = s.accept()
            print('new connection from', client_address)
            connection.setblocking(0)
            inputs.append(connection)
        else:
            data = s.recv(1024)
            if data:
                print('received "%s" from %s' % (data, s.getpeername()))
                s.send(data)
                print('sending data back to the client')
            else:
                print('closing', client_address, 'after reading no
