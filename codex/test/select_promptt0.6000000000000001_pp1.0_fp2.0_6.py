import select
# Test select.select()
# select.select() returns a tuple of three lists:
# 1st list: objects ready for reading
# 2nd list: objects ready for writing
# 3rd list: objects with errors

# select.select() blocks until one of the watched file descriptors is ready
# select.select() is a good way to build a simple network server

# Example:
# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set the socket to non-blocking
sock.setblocking(0)

# set up the socket connection
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

# sockets from which we expect to read
inputs = [sock]

# sockets from which we expect to write
outputs = []

