import select
# Test select.select
import socket
import os

# Create a non blocking socket
server = socket.socket()
server.bind(('127.0.0.1',0))
server.setblocking(0)
server.listen(5)

# Enable the epoll mechanism
epoll = select.epoll()

# Register the server for reading
epoll.register(server.fileno(), select.EPOLLIN)

# Create a log
log = open('log.txt', 'w')

