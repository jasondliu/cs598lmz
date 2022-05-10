import socket
# Test socket.if_indextoname
if_nametoindex = socket.if_indextoname(1)
if_indextoname = socket.if_nametoindex(if_nametoindex)

# Test socket.gethostname()
hostname = socket.gethostname()

# Test socket.gethostbyname()
hostbyname = socket.gethostbyname(hostname)

# Test socket.gethostbyname_ex()
hostbyname_ex = socket.gethostbyname_ex(hostname)

# Test socket.gethostbyaddr()
hostbyaddr = socket.gethostbyaddr(hostbyname)

# Test socket.getfqdn()
fqdn = socket.getfqdn(hostbyname)

# Test socket.getaddrinfo()
addrinfo = socket.getaddrinfo(fqdn, 80)

# Test socket.getnameinfo()
nameinfo = socket.getnameinfo(addrinfo[0][4], 80)

# Test socket.getservbyname()
servbyname = socket.getservbyname('http')

#
