import socket
# Test socket.if_indextoname
print("socket.if_indextoname({}) = {}".format(socket.if_nametoindex("eth0"), socket.if_indextoname(socket.if_nametoindex("eth0"))))

# Test socket.if_nameindex
print("socket.if_nameindex() = {}".format(socket.if_nameindex()))

# Test socket.if_nametoindex
print("socket.if_nametoindex({}) = {}".format("eth0", socket.if_nametoindex("eth0")))

# Test socket.getaddrinfo
print("socket.getaddrinfo({}, {}, {}, {}, {}) = {}".format("www.google.com", 80, socket.AF_INET, socket.SOCK_STREAM, socket.AI_CANONNAME, socket.getaddrinfo("www.google.com", 80)))

# Test socket.gethostbyaddr
print("socket.gethostbyaddr({}) = {}".format("216.58.193.78", socket.gethostbyaddr("216.58.193.78")))


