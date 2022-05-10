import select
# Test select.select().

import socket
import select

# Create an empty set.  We'll use it to store the descriptors
# that we want to wait for when we call select().
r = []

# Create two servers that echo the contents of the data
# sent to them.  Each echo server opens a TCP port and
# listens for connections on it.
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the SO_REUSEADDR socket option, so that we can start
# a server on a port immediately after the previous server
# is shutdown.  Without this option set, attempting to
# start a server on a port that was recently used by another
# server will fail.
server1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the two ports to localhost
