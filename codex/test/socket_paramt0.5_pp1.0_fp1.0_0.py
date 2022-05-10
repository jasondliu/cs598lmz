import socket
socket.if_indextoname(2)

#
print(socket.gethostname())
print(socket.gethostbyname_ex(socket.gethostname()))
print(socket.gethostbyname(socket.gethostname()))

#
print(socket.gethostbyaddr("220.181.111.188"))

#
print(socket.getprotobyname("tcp"))
print(socket.getservbyname("http"))
print(socket.getservbyport(80))

#
socket.getaddrinfo("www.baidu.com", 80)
socket.getaddrinfo("www.baidu.com", 80, 0, 0, socket.IPPROTO_TCP)
socket.getaddrinfo("www.baidu.com", 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

#
socket.getfqdn("www.baidu.com")

#
