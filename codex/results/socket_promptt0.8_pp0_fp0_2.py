import socket
# Test socket.if_indextoname()
if_indextoname(1) # ok
if_indextoname(2) # ok
if_indextoname('1') # crash
#p0
assert(True)

# Test socket.if_nameindex()
# FIXME: not supported by pypy
#if_nameindex() # crash
#p0
#assert(True)

# Test socket.gethostbyname()
try:
    gethostbyname(u'localhost') # ok
    gethostbyname('localhost') # ok
    # gethostbyname(2.0) # crash
except:
    pass

# Test socket.gethostbyname_ex()
try:
    gethostbyname_ex(u'localhost') # ok
    gethostbyname_ex('localhost') # ok
    # gethostbyname_ex(2.0) # crash
except:
    pass

# Test socket.gethostname()
gethostname() # ok

# Test socket.getprotobyname()
getprotobyname(b'udp') # ok

