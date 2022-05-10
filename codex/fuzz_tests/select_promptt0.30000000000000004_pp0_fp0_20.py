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
server_socket.send(request_data)

# Wait for a response

events = poller.poll(1)
print(events)
if events:
    data = client_socket.recv(1024)
    print("Received:", data)
else:
    print("No response within 1 seconds")

# Clean up

server_socket.close()
client_socket.close()
