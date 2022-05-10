import socket
# Test socket.if_indextoname
assert socket.if_indextoname(1) == b'lo'
# Test socket.if_indextoname
assert socket.if_indextoname(100) == b'eth0'
# Test socket.if_indextoname
assert socket.if_indextoname(200) == b'eth1'
# Test socket.if_indextoname
assert socket.if_indextoname(300) == b'eth2'
# Test socket.if_indextoname
assert socket.if_indextoname(400) == b'eth3'
# Test socket.if_indextoname
assert socket.if_indextoname(500) == b'eth4'
# Test socket.if_indextoname
assert socket.if_indextoname(600) == b'eth5'
# Test socket.if_indextoname
assert socket.if_indextoname(700) == b'eth6'
# Test socket.if_indextoname
