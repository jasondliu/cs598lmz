import socket
# Test socket.if_indextoname
import socket
print socket.if_indextoname(1)
# Test socket.if_nameindex
import socket
print socket.if_nameindex()
# Test socket.if_nametoindex
import socket
print socket.if_nametoindex('lo')
# Test socket.getservbyname
import socket
print socket.getservbyname('http')
# Test socket.getservbyport
import socket
print socket.getservbyport(80)
# Test socket.gethostbyname
import socket
print socket.gethostbyname('localhost')
# Test socket.gethostbyname_ex
import socket
print socket.gethostbyname_ex('localhost')
# Test socket.gethostname
import socket
print socket.gethostname()
# Test socket.gethostbyaddr
import socket
print socket.gethostbyaddr('127.0.0.1')
# Test socket.getprotobyname
import socket
print socket.getprotobyname('tcp')
# Test socket.getprotobynumber
import socket
print socket.getprotobynumber(
