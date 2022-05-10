import socket
socket.if_indextoname(0x1)

# Get the socket name
s.getsockname()

# Get the peer name
s.getpeername()

# Send data to the server
s.send(b'Hi there, server')

# Receive data from the server
s.recv(1024)

# Close the connection
s.close()
```

### UDP

```python
import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
s.sendto(b'Hi there, server', ('127.0.0.1', 8888))

# Receive data from the server
s.recvfrom(1024)

# Close the connection
s.close()
```

## Python Networking

### Simple Web Server

```python
import socket

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address =
