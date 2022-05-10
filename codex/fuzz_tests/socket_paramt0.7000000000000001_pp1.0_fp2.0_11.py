import socket
socket.if_indextoname(3)

print(socket.gethostbyname(socket.gethostname()))

print(socket.gethostbyaddr("127.0.0.1"))

print(socket.getservbyport(80))

print(socket.getservbyname("http"))

print(socket.getprotobyname("udp"))

print(socket.getaddrinfo("www.example.com", 80, 0, 0, socket.IPPROTO_TCP))

print(socket.getaddrinfo("www.example.com", 80, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP, socket.AI_CANONNAME))

print(socket.getaddrinfo("www.example.com", None, socket.AF_INET, socket.SOCK_STREAM))


print("\n\n")
# 枚举出所有域名别名
print(socket.gethostbyname_ex("www.example.com"))
print(socket.getfqdn("localhost"))

