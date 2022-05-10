import select
# Test select.select()

import socket

# HOST = '127.0.0.1'
HOST = '10.211.55.20'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connection_list = [server_socket]
while True:
    print '  before select...'
    read_sockets, write_sockets, error_sockets = select.select(connection_list, [], [])
    print '  after select...'

    for s in read_sockets:
        if s is server_socket:
            print '  a new client comes in'
            client_socket, addr = s.accept()
            connection_list.append(client_socket)
        else:
            data = s.recv(1024)
            if data:
                print '
