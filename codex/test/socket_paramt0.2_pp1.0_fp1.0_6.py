import socket
socket.if_indextoname(3)

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
s.connect(("www.google.com", 80))

# Send some data
s.send("GET / HTTP/1.0\n\n".encode())

# Receive a response
response = s.recv(4096)

# Close the connection
s.close()

print(response)

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
s.connect(("www.google.com", 80))

# Send some data
s.send("GET / HTTP/1.0\n\n".encode())

# Receive a response
response = s.recv(4096)

# Close the connection
s.close()

print(response)

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to
