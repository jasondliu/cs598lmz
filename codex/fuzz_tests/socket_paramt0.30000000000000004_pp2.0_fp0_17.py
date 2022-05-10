import socket
socket.if_indextoname(3)

# Connect to the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))

# Send the data
s.send(b'Hello, world')

# Receive the data
data = s.recv(1024)
print(data)

# Close the connection
s.close()
