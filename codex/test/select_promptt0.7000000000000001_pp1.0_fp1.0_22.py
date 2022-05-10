import select
# Test select.select()

# Socket reference: https://docs.python.org/3/howto/sockets.html

# 1. Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. Bind the socket to a port
sock.bind(('127.0.0.1', 8888))
# 3. Listen for connection
sock.listen(5)

# For simplicity, one client
clients = []

while True:
    # This call blocks until a connection or an error
    # select.select(rlist, wlist, xlist[, timeout])
    r, w, x = select.select([sock] + clients, [], [])
    # The call returns 3 lists:
    #  r: objects ready for reading
    #  w: objects ready for writing
    #  x: objects with exceptions

