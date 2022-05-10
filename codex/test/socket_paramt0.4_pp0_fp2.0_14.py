import socket
socket.if_indextoname(3)

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
s.connect(("www.google.com", 80))

# Send data
s.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# Receive data
data = s.recv(1024)
print(data)

# Close the connection
s.close()

# Create a server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8080))
s.listen(5)

# Accept connections
while True:
    client, address = s.accept()
    request = client.recv(1024)
    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    client.send(b"Hello World!")
    client.close()

# Create a server
import socket
s
