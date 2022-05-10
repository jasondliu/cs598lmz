import socket
# Test socket.if_indextoname
print("if_indextoname:", socket.if_indextoname(1))
# Test socket.if_nameindex
print("if_nameindex:", socket.if_nameindex())
# Test socket.if_nametoindex
print("if_nametoindex:", socket.if_nametoindex("lo"))
# Test socket.getaddrinfo
print("getaddrinfo:", socket.getaddrinfo("localhost", 8080))
# Test socket.getfqdn
print("getfqdn:", socket.getfqdn("localhost"))
# Test socket.gethostbyaddr
print("gethostbyaddr:", socket.gethostbyaddr("127.0.0.1"))
# Test socket.gethostbyname
print("gethostbyname:", socket.gethostbyname("localhost"))
# Test socket.gethostbyname_ex
print("gethostbyname_ex:", socket.gethostbyname_ex("localhost"))
# Test socket.gethostname
print("gethostname:", socket.gethostname())
# Test socket.getnameinfo

