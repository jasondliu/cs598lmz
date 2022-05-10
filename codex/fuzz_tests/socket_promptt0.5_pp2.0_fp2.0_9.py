import socket
# Test socket.if_indextoname()

import socket
import sys

if len(sys.argv) > 1:
    index = int(sys.argv[1])
else:
    index = socket.if_nametoindex("lo")

print("lo:", index, socket.if_indextoname(index))

# TODO: What to do on Windows?  If there is more than one interface,
# how to get a valid index?
# TODO: What to do on Windows with Python 3.4?  if_indextoname() is
# missing.
