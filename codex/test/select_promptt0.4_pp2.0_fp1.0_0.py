import select
# Test select.select

# Create a pair of connected sockets
server, client = socket.socketpair()

# Make each non-blocking
server.setblocking(0)
client.setblocking(0)

# Fill server's send buffer
server.send(b'x' * 100000)

# Peek at client to see when data is available
while True:
    try:
        response = select.select([client], [], [])
        print(response)
        client.recv(100)
    except BlockingIOError:
        pass
    else:
        break

