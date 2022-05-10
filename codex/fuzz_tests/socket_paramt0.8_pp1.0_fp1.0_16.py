import socket
socket.if_indextoname(12)

# The socket address is a tuple consisting of an IP address and a port number.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 50000))

s.listen(1)  # Listen for connections made to the socket.
# The argument to listen is the number of connections to accept before refusing new connections.

try:
    # The accept method of a socket object returns a new socket object representing the connection.
    # It also returns the address of the client.
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)  # The data received is a binary string.
        print 'Received', repr(data)
        if data:
            conn.sendall(data)  # If there is data, send it back to the client.
        else:
            break
finally:
    conn.close()

# File-like objects
# The socket object has a makefile method that performs the same function
