import socket
# Test socket.if_indextoname
if_indextoname = socket.if_indextoname
if_indextoname(0)
if_indextoname(0, "foo")
if_indextoname(0, "foo", "bar")

# Test socket.if_nameindex
if_nameindex = socket.if_nameindex
for i in if_nameindex():
    pass

# Test socket.if_nametoindex
if_nametoindex = socket.if_nametoindex
if_nametoindex("lo")

# Test socket.setdefaulttimeout
setdefaulttimeout = socket.setdefaulttimeout
setdefaulttimeout(0.1)
setdefaulttimeout(None)

# Test socket.getaddrinfo
getaddrinfo = socket.getaddrinfo
getaddrinfo("www.python.org", 80)
getaddrinfo("www.python.org", 80, 0, 0, socket.IPPROTO_TCP)
getaddrinfo("www.python.org", 80, 0, 0, socket.IPPROTO_TCP, socket.AI_PASSIVE)
getaddrinfo("www
