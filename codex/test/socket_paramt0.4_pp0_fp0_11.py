import socket
socket.if_indextoname(3)

socket.gethostbyname('www.google.com')

import telnetlib

tn = telnetlib.Telnet('www.google.com', 80)
tn.write('GET / HTTP/1.0\n\n')

