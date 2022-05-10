import select
# Test select.select()

# Create a pair of connected sockets

server_socket, client_socket = socket.socketpair()

# Set up the poller

poller = select.poll()
poller.register(client_socket, select.POLLIN)

# Send a datagram

request_data = b"Hello, world!"
print("Sending:", request_data)
