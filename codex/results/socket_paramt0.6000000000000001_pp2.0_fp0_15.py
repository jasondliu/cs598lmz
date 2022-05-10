import socket
socket.if_indextoname(3)

# Get the IP address of the interface
import socket
socket.if_nameindex()

# Get the MAC address of the interface
import uuid
print(hex(uuid.getnode()))

# Get the MAC address of the interface
import uuid
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

# Get the IP address of the interface
import socket
socket.gethostbyname(socket.gethostname())

# Get the IP address of the interface
import socket
socket.gethostbyname_ex(socket.gethostname())

# Get the IP address of the interface
import socket
socket.gethostname()

# Get the IP address of the interface
import socket
socket.gethostbyname(socket.gethostname())

# Get the IP address of the interface
import socket
socket.gethostbyname_ex(socket.gethostname())

# Get the IP address of the interface

