import socket
# Test socket.if_indextoname()
if_indextoname = socket.if_indextoname
if_indextoname(1)
# Test socket.if_nameindex()
if_nameindex = socket.if_nameindex
if_nameindex()
# Test socket.if_nameindex() with again
if_nameindex()

# Test socket.gethostbyname_ex()
gethostbyname_ex = socket.gethostbyname_ex
gethostbyname_ex('localhost')
gethostbyname_ex('localhost', socket.AF_INET)
gethostbyname_ex('localhost', socket.AF_INET6)
# Test socket.gethostbyname_ex() with again
gethostbyname_ex('localhost')
gethostbyname_ex('localhost', socket.AF_INET)
gethostbyname_ex('localhost', socket.AF_INET6)

# Test socket.gethostbyaddr()
gethostbyaddr = socket.gethostbyaddr
gethostbyaddr('127.0.0.1')
gethostbyaddr('::1')
# Test
