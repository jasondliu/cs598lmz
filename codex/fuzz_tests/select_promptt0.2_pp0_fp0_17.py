import select
# Test select.select

def test_select():
    import os
    import select
    import socket
    import sys
    import time

    # Create a pair of connected sockets
    if sys.platform == 'win32':
        test_sockets = socket.socket, socket.socket
    else:
        test_sockets = socket.socketpair()

    # Connect the sockets to a pair of file descriptors
    read_fd = test_sockets[0].fileno()
    write_fd = test_sockets[1].fileno()

    # Set the sockets to non-blocking mode
    for s in test_sockets:
        s.setblocking(False)

    # Create a pair of connected sockets
    if sys.platform == 'win32':
        test_sockets = socket.socket, socket.socket
    else:
        test_sockets = socket.socketpair()

    # Connect the sockets to a pair of file descriptors
    read_fd = test_sockets[0].fileno()
    write_fd = test_sockets[1].fileno()

    # Set the sockets to non
