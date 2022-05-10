import socket
# Test socket.if_indextoname()

# Simple check, just to make sure the function exists.

from socket import if_indextoname

if_indextoname(1)

# This is a very unlikely name, but should still be valid.

if_indextoname(1, 'a' * 1024)

# An empty string is valid too.

if_indextoname(1, '')

# Invalid index.

try:
    if_indextoname(-1)
except OSError:
    pass

try:
    if_indextoname(1, 'a' * 1024, 'a' * 1024)
except TypeError:
    pass
