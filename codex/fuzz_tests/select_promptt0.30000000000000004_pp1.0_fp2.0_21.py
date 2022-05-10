import select
# Test select.select()

# Create a pair of connected sockets

if os.name == 'posix':
    # On Unix, the sockets will be using the file descriptor numbers
    # returned by the socket() call.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 0))
    server.listen(1)
    client.connect(server.getsockname())
    server_fd = server.fileno()
    client_fd = client.fileno()
else:
    # On Windows, the sockets will be using the small integer handles
    # returned by the socket() call.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 0))
    server.listen(1)
    client.connect(server.getsockname())
    server
