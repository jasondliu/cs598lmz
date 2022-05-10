import select
# Test select.select()

import socket
import sys

port = 10000

server = socket.socket()
server.bind(("", port))
server.listen(1)

sock_list = [server]

while True:
    r, w, x = select.select(sock_list, [], [])
    for sock in r:
        if sock is server:
            client, addr = server.accept()
            sock_list.append(client)
        else:
            client.send(sys.stdin.read())
