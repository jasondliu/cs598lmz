import select
# Test select.select

def main():
    # Create a pair of connected sockets
    if len(sys.argv) != 3:
        sys.exit('Usage: python select_echo_server.py interface "message"')
    interface = sys.argv[1]
    message = sys.argv[2]

    sock1, sock2 = socket.socketpair()

    # Set larger recv buffer sizes on each socket
    sock1.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
    sock2.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)

    print 'Starting up on %s port %s' % sock1.getsockname()
    print 'Starting up on %s port %s' % sock2.getsockname()

    # Create a pair of connected sockets
    sock1.sendall(message)
    sock2.sendall(message)

    # Use select() to wait until each socket is readable
    readable, writable, exceptional = select.select([sock1
