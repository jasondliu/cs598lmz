import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(('127.0.0.1', 8000))

# Send a message
s.sendall('Hello, world')

# Receive a response
response = s.recv(1024)
print(response)

# Close the connection
s.close()
