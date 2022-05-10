import select
# Test select.select()

import socket

sock = socket.socket()
sock.bind(('', 0))
sock.listen(5)

# select.select() takes three lists of file descriptors: those to be
# checked for readability, those to be checked for writability, and
# those to be checked for errors.

# In this case, we're only interested in readability, so we pass
# empty lists for the other two.

r, w, e = select.select([sock], [], [])

# The return value is a triple of lists of file descriptors.
# The first list contains those that are readable;
# the second contains those that are writable;
# the third contains those that have errors.

# In this case, we expect the first list to contain the listening
# socket, since we're expecting a client to connect.

