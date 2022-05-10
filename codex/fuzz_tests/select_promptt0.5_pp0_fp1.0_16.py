import select
# Test select.select

import os
import select
import socket
import sys
import time

host = ''
port = 50000
backlog = 5
size = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(backlog)
timeout = 10
input = [server,sys.stdin]
running = 1
while running:
    inputready,outputready,exceptready = select.select(input,[],[],timeout)

    # Timeout
    if not inputready:
        print "Server timeout. Doing some other work here"

    for s in inputready:

        if s == server:
            # handle the server socket
            client, address = server.accept()
            input.append(client)
            print "Client connected from", address

        elif s == sys.stdin:
            # handle standard input
            junk = sys.stdin.readline()
            running = 0

        elif s: # client socket
            data = s.recv(size)
            if data:
                print
