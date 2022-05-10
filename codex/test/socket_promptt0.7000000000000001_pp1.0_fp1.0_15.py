import socket
# Test socket.if_indextoname()
assert socket.if_indextoname(1) == 'lo'
# Test socket.if_nameindex()
assert socket.if_nameindex()[0][1] == 1
# Test socket.if_nametoindex()
assert socket.if_nametoindex('lo') == 1

# Test netmask_ntoa()
#assert socket.netmask_ntoa('\xFF\xFF\xFF\xFF' == '255.255.255.255'

# Test getaddrinfo()
assert socket.getaddrinfo('www.python.org', 80) == socket.getaddrinfo(socket.gethostname(), 80)

# Test getnameinfo()
assert socket.getnameinfo(('127.0.0.1', 80), 0) == socket.gethostname(), socket.gethostbyname('www.python.org')

# Test gethostbyname()
assert socket.gethostbyname('www.python.org') == socket.gethostname()

# Test gethostbyname_ex()
