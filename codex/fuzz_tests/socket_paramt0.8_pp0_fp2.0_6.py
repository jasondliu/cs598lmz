import socket
socket.if_indextoname(3)
print(socket.if_indextoname(3))
print(socket.if_nameindex())

# get hostname
print(socket.gethostname())

# server fd = socket.socket()
# server fd.bind(host, port) # port should be greater than 1024
# server fd.listen(backlog) # listen for connection
# connection_fd, client_addr = server fd.accept() # block until a connection is made
#   # connection_fd is a new socket fd used for the actual communication
# server fd.close() # close the listening socket

# client fd = socket.socket()
# client fd.connect(addr) # open connection to a remote host
# client fd.close() # terminals connection, may be client or server
