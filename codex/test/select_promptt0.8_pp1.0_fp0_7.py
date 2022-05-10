import select
# Test select.select
import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 9999))
server.listen(5)

inputs = [server]
outputs = []

while True:
    readable, writable, exceptional = select.select(inputs, outputs, [])
    print('-- New Loop --')
    for sock in readable:
        if sock is server:
            connection, client_address = sock.accept()
            print('Connection from', client_address)
            inputs.append(connection)
        else:
            print('Got data from', sock.getpeername())
            data = sock.recv(1024)
            print(data)
            if data:
                outputs.append(sock)
            else:
                sock.close()
                inputs.remove(sock)
    for sock in writable:
        sock.send(b'ACK!')
        outputs.remove(sock)
