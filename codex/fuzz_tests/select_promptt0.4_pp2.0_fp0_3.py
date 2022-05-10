import select
# Test select.select()
#
# select.select() is a function that takes 3 lists of file descriptors and
# waits until one of them is ready for reading, writing, or has an exception
# (depending on which list it's in).
#
# This is a very simple test which waits for a socket to be ready for reading
# and then calls recv() on it.
#
# This test is in the public domain.
#
# Eli Bendersky [http://eli.thegreenplace.net]
# This code is in the public domain.
import socket
import select

# Create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a public host, and a well-known port
serversocket.bind(("localhost", 8080))
# Become a server socket
serversocket.listen(5)

while True:
    # Wait for a connection
    connection, address = serversocket.accept()
    print("Got connection from", address)
    # Wait for data
    # Note that select()
