import socket
# Test socket.if_indextoname(3)
print socket.if_indextoname(3)
# Test socket.if_nameindex(3)
print socket.if_nameindex()
# Test socket.if_nametoindex(3)
print socket.if_nametoindex("lo")
# Test socket.gethostbyname_ex(3)
print socket.gethostbyname_ex("localhost")
# Test socket.gethostbyaddr(3)
print socket.gethostbyaddr("127.0.0.1")
# Test socket.getservbyname(3)
print socket.getservbyname("ftp")
# Test socket.getservbyport(3)
print socket.getservbyport(80)
# Test socket.getprotobyname(3)
print socket.getprotobyname("tcp")
# Test socket.getaddrinfo(3)
print socket.getaddrinfo("www.python.org", 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
# Test socket.gethostbyname(3)

