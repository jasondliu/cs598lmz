import socket
# Test socket.if_indextoname
assert socket.if_indextoname(0) == b'lo'
# Test socket.if_nameindex
assert socket.if_nameindex() == [(1, b'lo')]
# Test socket.if_nametoindex
assert socket.if_nametoindex(b'lo') == 1
# Test socket.gethostbyaddr
assert socket.gethostbyaddr(b'127.0.0.1') == ('localhost', [], [b'127.0.0.1'])
# Test socket.gethostbyname_ex
# Test socket.gethostbyname
assert socket.gethostbyname(b'localhost') == '127.0.0.1'
# Test socket.getnameinfo
assert socket.getnameinfo((b'localhost', 0), 0) == ('localhost', '0')
# Test socket.getprotobyname
assert socket.getprotobyname('tcp') == 6
# Test socket.getservbyname
assert socket.getservbyname('ssh', 'tcp') == 22
# Test socket.getservbyport
