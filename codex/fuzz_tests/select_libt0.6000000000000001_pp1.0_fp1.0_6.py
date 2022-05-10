import selectors

# Some constants
SERVER_HOST = 'localhost'
SERVER_PORT = 5001
RECV_BUFFER_SIZE = 4096

# Set up the selector to poll for "read" readiness on the socket
sel = selectors.DefaultSelector()

# Define a message handler for when a socket is ready to read
def handle_echo(sock, mask):
    try:
        data = sock.recv(RECV_BUFFER_SIZE)
    except BlockingIOError:
        # Resource temporarily unavailable (errno EWOULDBLOCK)
        pass
    else:
        if data:
            print('received {!r}'.format(data))
        else:
            print('closing connection to', sock.getpeername())
            sel.unregister(sock)
            sock.close()

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set the socket to non-blocking mode
sock.setblocking(False)
# Connect the socket to the server
sock.connect
