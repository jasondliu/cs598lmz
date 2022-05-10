import select
# Test select.select()
#
# Create a pair of connected sockets
import socket

def test():
    s1, s2 = socket.socketpair()
