import select
# Test select.select()

# Create a pair of connected sockets

if os.name == 'posix':
    # On Unix, the sockets will be using file descriptors
    # so we can use the select() call on them directly
    server, client = socket.socketpair()
else:
    # On Windows, socketpair() is not available, so we must
    # build the socket pair ourselves.
    # We create a connected TCP/IP socket and use the
    # resulting socket pair for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 0))
    server.listen(1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server.getsockname())
    server = server.accept()[0]

# Set the sockets to be non-blocking

client.setblocking(0)
server.setblocking(0)

# Send some data from the client to the server

client.send(b'Hello')
