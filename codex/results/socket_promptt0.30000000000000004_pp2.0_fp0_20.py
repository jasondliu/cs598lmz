import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except socket.error:
    pass
else:
    raise TestFailed, 'if_indextoname(1) should have failed'

# Test socket.if_nameindex()
try:
    socket.if_nameindex()
except socket.error:
    pass
else:
    raise TestFailed, 'if_nameindex() should have failed'

# Test socket.if_nametoindex()
try:
    socket.if_nametoindex('lo')
except socket.error:
    pass
else:
    raise TestFailed, 'if_nametoindex(\'lo\') should have failed'

# Test socket.gethostbyname_ex()
try:
    socket.gethostbyname_ex('localhost')
except socket.error:
    pass
else:
    raise TestFailed, 'gethostbyname_ex(\'localhost\') should have failed'

# Test socket.getnameinfo()
try:
    socket.getnameinfo(('127.0.0.
