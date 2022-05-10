import socket
socket.if_indextoname(3)

# Q4
import struct, socket
socket.inet_ntoa(struct.pack("!L", 0x7f000001))

# Q5
import socket
socket.gethostbyname("localhost")

# Q6
import socket
socket.gethostbyname_ex("localhost")

# Q7
import socket
socket.gethostbyaddr("127.0.0.1")

# Q8
import socket
socket.getservbyname("http")

# Q9
import socket
socket.getservbyport(80)

# Q10
import socket
socket.getprotobyname("tcp")

# Q11
import socket
socket.getdefaulttimeout()

# Q12
import socket
socket.setdefaulttimeout(0.5)

# Q13
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
s.sendall("GET /\r\n")
s.recv(1024)

# Q
