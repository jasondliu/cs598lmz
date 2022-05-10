import socket
# Test socket.if_indextoname
socket.if_indextoname(1)
socket.if_indextoname(1, 'test')

# Test socket.if_nameindex
socket.if_nameindex()

# Test socket.if_nametoindex
socket.if_nametoindex('lo')
socket.if_nametoindex('lo', 'test')

# Test socket.getfqdn
socket.getfqdn()
socket.getfqdn('localhost')
socket.getfqdn('127.0.0.1')

# Test socket.gethostname
socket.gethostname()

# Test socket.gethostbyname, socket.gethostbyname_ex
socket.gethostbyname('localhost')
socket.gethostbyname_ex('localhost')

# Test socket.gethostbyaddr
socket.gethostbyaddr('127.0.0.1')

# Test socket.getnameinfo
socket.getnameinfo(('127.0.0.1', 80), 0)
socket.getnameinfo(('127.0.0.1', 80),
