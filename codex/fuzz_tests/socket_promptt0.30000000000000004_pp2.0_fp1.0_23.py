import socket
# Test socket.if_indextoname
if_indextoname = socket.if_indextoname(1)
print if_indextoname

# Test socket.if_nametoindex
if_nametoindex = socket.if_nametoindex(if_indextoname)
print if_nametoindex

# Test socket.gethostbyname
gethostbyname = socket.gethostbyname('localhost')
print gethostbyname

# Test socket.gethostbyname_ex
gethostbyname_ex = socket.gethostbyname_ex('localhost')
print gethostbyname_ex

# Test socket.gethostbyaddr
gethostbyaddr = socket.gethostbyaddr('127.0.0.1')
print gethostbyaddr

# Test socket.gethostname
gethostname = socket.gethostname()
print gethostname

# Test socket.gethostname
gethostname = socket.gethostname()
print gethostname

# Test socket.getprotobyname
getprotobyname = socket.getprotobyname('tcp')
print
