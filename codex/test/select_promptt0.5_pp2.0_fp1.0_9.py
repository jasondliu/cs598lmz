import select
# Test select.select()

import socket

# Create two sockets.
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind them to the same port.
s1.bind(('127.0.0.1', 0))
s2.bind(('127.0.0.1', s1.getsockname()[1]))

# Connect the first to the second.
s1.connect(s2.getsockname())

# Set s1 to be non-blocking.
s1.setblocking(False)

# s1 is now ready to read.
assert select.select([s1], [], []) == ([s1], [], [])

# s1 is not ready to write.
assert select.select([], [s1], []) == ([], [], [])

# s1 is not ready to read or write.
assert select.select([s1], [s1], []) == ([], [], [])

