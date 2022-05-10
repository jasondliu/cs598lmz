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

try:
  # Create a map to store file objects
  fd_to_socket = {server.fileno():server}
  
  # Create an event loop
  while True:
    # Process the events
    for fd,events in epoll.poll(1):
      sock = fd_to_socket[fd]

      # If it is EPOLLIN event
      if events & select.EPOLLIN:
        # If it is the listening socket
        if sock == server:
          connection, addr = server.accept()
          connection.setblocking(0)
          
         
