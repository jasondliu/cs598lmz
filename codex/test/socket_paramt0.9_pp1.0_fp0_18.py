import socket
socket.if_indextoname(8)

#Note: The value might be 'lo' if you don't have eth0 or wifi set up.

# 9.4.4

import socket
socket.if_nametoindex('eth0')

# 9.4.5

import socket
# Displays a tuple of all the network interfaces.
#    Each tuple contains (name, index, FAMILY, MAC_ADDRESS,
#                        IP, SUBNET_MASK)
socket.if_nameindex()

# 9.4.6

# Socket
import socket
SERVER = 'www.google.com'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER,PORT))
query = "GET / HTTP/1.1\r\n\r\n"
request = s.send(query.encode())
response = s.recv(4096)
print(response)

# Raw Socket
import socket
PROTOCOL = socket.IPPROTO_TCP
