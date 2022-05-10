import select
# Test select.select()
# select() takes 3 lists:
# 1. The first list contains all sockets we want to be able to read from.
# 2. The second list contains all sockets we want to be able to write to.
# 3. The third list contains all sockets we want to check for errors.
# It then waits until one of the sockets in the first two lists is ready for reading or writing.
# When this happens, it returns the lists of all three.

# Example
# We create a socket and connect to a server.
# We then call select() and check if it's ready for reading.
# If so, we read the data and print it.
# If not, we wait 1 second and try again.

import socket, select

s = socket.socket()

# connect to localhost on port 5000
s.connect(('127.0.0.1', 5000))

