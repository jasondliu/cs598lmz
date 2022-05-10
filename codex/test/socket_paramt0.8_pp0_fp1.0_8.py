import socket
socket.if_indextoname(4)

"getaliasbyip"
import socket
socket.gethostbyaddr("8.8.8.8")

"gethostbyname_ex"
import socket
socket.gethostbyname_ex("www.python.org")

"gethostname"
import socket
socket.gethostname()

"gethostbyname"
import socket
socket.gethostbyname('www.python.org')

"getfqdn"
import socket
socket.getfqdn("8.8.8.8")

"getaddrinfo"
import socket
socket.getaddrinfo("www.python.org",80,0,0,socket.IPPROTO_TCP)

"getdefaulttimeout"
import socket
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(3)
print(socket.getdefaulttimeout())

"getnameinfo"
import socket
socket.getnameinfo(('8.8.8.8',80),0)

"getservbyport"
import socket
socket.getservbyport(80)


