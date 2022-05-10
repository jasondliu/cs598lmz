import socket
socket.if_indextoname(2)

socket.gethostbyname("www.google.com")
socket.gethostbyname_ex("www.google.com")

hostname=socket.gethostname()
socket.gethostbyname(hostname)

#see what ports are open on my machine
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)

ip_range=socket.gethostbyname_ex(ip)[-1]
print(ip_range)
print(type(ip_range))

import sys
print(sys.path)
