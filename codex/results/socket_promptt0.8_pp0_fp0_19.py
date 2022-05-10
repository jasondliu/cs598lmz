import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test socket.if_nametoindex
print(socket.if_nametoindex("eth0"))
# Test socket.gethostbyname
print(socket.gethostbyname("localhost"))
# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("www.baidu.com"))
# Test socket.gethostname
print(socket.gethostname())
# Test socket.gethostbyaddr
print(socket.gethostbyaddr("127.0.0.1"))
# Test socket.getnameinfo
print(socket.getnameinfo())
# Test socket.getprotobyname
print(socket.getprotobyname("tcp"))
# Test socket.getservbyname
print(socket.getservbyname("ssh"))
# Test socket.getdefaulttimeout
print(socket.getdefaulttimeout())
# Test socket.setdefaulttimeout
# socket.setdefaulttimeout(3)
# print(socket.getdefaulttimeout())
# Test socket.getaddrinfo
print(socket.get
