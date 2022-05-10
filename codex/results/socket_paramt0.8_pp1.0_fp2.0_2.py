import socket
socket.if_indextoname(3)

# SOCK_DGRAM is the socket type to use for UDP sockets
# socket.SOCK_DGRAM

# SOCK_STREAM is the socket type to use for TCP sockets
# socket.SOCK_STREAM

# you can use this to get all of the interfaces on the system and their indexes
# socket.if_nameindex()

# AF_INET is the address family ipv4
# socket.AF_INET

# AF_INET6 is the address family ipv6
# socket.AF_INET6

# SOCK_RAW is a powerful socket type. For more details: http://sock-raw.org/papers/sock_raw
# socket.SOCK_RAW
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(10)
while True:
    try:
        client, address = s.accept()
        while True:
            data = client.recv(10)
            if not data:
                break
           
