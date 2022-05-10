import select
# Test select.select()

# First, build a pair of connected sockets

import socket, sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 0))
server.listen(1)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server.getsockname())

# Now, pass them to select()

readable, writable, exceptional = select.select(
    [client, server], [], [],
    )

for sock in readable:
    if sock is server:
        connection, client_address = sock.accept()
        connection.close()
    else:
        data = sock.recv(1024)
        if data:
            sock.sendall(data)
        else:
            sock.close()
            server.close()
            sys.exit()

# Now, try passing them to select() with a timeout

readable, writable, exceptional = select.select(
    [client, server], [], [],
    1.
