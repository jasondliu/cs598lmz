import socket
# Test socket.if_indextoname()
ifname = socket.if_indextoname(1)
print(ifname)

# Test socket.if_nameindex()
if_nameindex = socket.if_nameindex()
print(if_nameindex)

# Test socket.if_nametoindex()
ifindex = socket.if_nametoindex('eth0')
print(ifindex)

# Test socket.gethostbyname()
ip = socket.gethostbyname('www.python.org')
print(ip)

# Test socket.gethostbyname_ex()
ip = socket.gethostbyname_ex('www.python.org')
print(ip)

# Test socket.gethostbyaddr()
host = socket.gethostbyaddr('216.58.209.110')
print(host)

# Test socket.gethostname()
hostname = socket.gethostname()
print(hostname)

# Test socket.gethostbyname_ex()
host = socket.gethostbyname_ex(hostname)
print(host)

# Test socket.get
