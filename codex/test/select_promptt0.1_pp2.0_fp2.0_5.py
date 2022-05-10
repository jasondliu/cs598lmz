import select
# Test select.select()

# Create a pair of connected sockets

# Create a pair of connected sockets

def test_select():
    import select
    import socket
    import sys
    import time

    s1, s2 = socket.socketpair()
    s1.setblocking(0)
    s2.setblocking(0)

