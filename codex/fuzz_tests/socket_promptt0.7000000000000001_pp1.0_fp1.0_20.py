import socket
# Test socket.if_indextoname()
if_indextoname = socket.if_indextoname(1)
print if_indextoname

# Test socket.if_nametoindex()
if_nametoindex = socket.if_nametoindex('lo')
print if_nametoindex

# Test socket.if_nameindex()
if_nameindex = socket.if_nameindex()
print if_nameindex

# Test socket.gethostbyname()
hostname = socket.gethostname()
hostbyname = socket.gethostbyname(hostname)
print hostbyname

# Test socket.gethostbyname_ex()
hostbyname_ex = socket.gethostbyname_ex(hostname)
print hostbyname_ex

# Test socket.gethostbyname_ex()
hostbyname_ex = socket.gethostbyname_ex(hostname)
print hostbyname_ex

# Test socket.gethostbyaddr()
hostbyaddr = socket.gethostbyaddr(hostbyname)
print hostbyaddr

# Test socket.getaddrinfo()
