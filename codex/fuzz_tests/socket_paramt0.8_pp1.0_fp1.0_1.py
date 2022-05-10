import socket
socket.if_indextoname(socket.if_nametoindex("wlp1s0"))

#!/usr/bin/env python3

import socket
socket.getaddrinfo("www.python.org", 80)

#!/usr/bin/env python3

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
s.sendall(b"GET / HTTP/1.0\r\n\r\n")

#!/usr/bin/env python3

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
s.sendall(b"GET / HTTP/1.0\r\n\r\n")

while True:
    data = s.recv(1024)
    if not data:
        break
    print(data)
s.close()

#!/usr/bin/env python3

import socket
s = socket.socket(socket.AF
