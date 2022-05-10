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

