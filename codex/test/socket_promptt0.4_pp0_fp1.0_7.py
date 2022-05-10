import socket
# Test socket.if_indextoname()
socket.if_indextoname(1)

# Test socket.getaddrinfo()
socket.getaddrinfo("www.python.org", 80, socket.AF_INET, socket.SOCK_STREAM,
                   socket.IPPROTO_TCP, socket.AI_CANONNAME)

# Test socket.getnameinfo()
socket.getnameinfo(("127.0.0.1", 80), socket.NI_NUMERICHOST)

# Test socket.gethostbyname()
socket.gethostbyname("www.python.org")

# Test socket.gethostbyname_ex()
socket.gethostbyname_ex("www.python.org")

# Test socket.gethostbyaddr()
socket.gethostbyaddr("127.0.0.1")

# Test socket.getfqdn()
socket.getfqdn("127.0.0.1")

# Test socket.gethostname()
socket.gethostname()

# Test socket.getprotobyname()
