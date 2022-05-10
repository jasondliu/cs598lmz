import select
# Test select.select on file descriptors

import support, time, socket

# Create sockets.
s1, s2 = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)
s3, s4 = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)

# Test "exceptional conditions" that no one cares about.
t, w, x = select.select([], [], [s2], 0)
t, w, x = select.select([], [], [s2])

# Create a file descriptor in read and write mode.
