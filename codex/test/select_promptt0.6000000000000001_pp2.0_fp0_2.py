import select
# Test select.select() using a socket

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 10000))
server.listen(5)

server.setblocking(0)

inputs = [ server ]
outputs = [ ]

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print('connection from', client_address)
            connection.setblocking(0)
            inputs.append(connection)
        else:
            data = s.recv(1024)
            if data:
                print('received', repr(data), 'from', s.getpeername())
                outputs.append(s)
            else:
                print('closing', client_address)
                inputs.remove(s)
                s.close()

    for s in writable:
        s.send('ack')
