import select
# Test select.select
#
# The following program uses select() to check for activity on three
# sockets. It starts two clients, each of which sends a short message
# to the server, then exits. The server selects() on the three sockets
# and prints any input received.
#
# To test, run this server in one window, then run the clients in two
# other windows.

import socket
import sys
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(5)
input = [server]

running = 1
while running:
    inputready,outputready,exceptready = select.select(input,[],[])

    for s in inputready:

        if s == server:
            # handle the server socket
            client, address = server.accept()
            input.append(client)

        elif s == sys.stdin:
            # handle standard input
            junk = sys.stdin.readline()
            running = 0

        else:
            # handle all other sockets
            data
