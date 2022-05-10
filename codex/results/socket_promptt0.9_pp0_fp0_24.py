import socket
# Test socket.if_indextoname
socket.if_indextoname
# Test socket.if_nameindex
socket.if_nameindex
# Test socket.if_nameindex

# The array of element should consist of tuples with two elements.
try:
    r = socket.if_nameindex(42)
except TypeError:
    assert True
else:
    assert False
try:
    r = socket.if_nameindex([])
except TypeError:
    assert True
else:
    assert False
try:
    r = socket.if_nameindex([(i,) for i in range(5)])
except TypeError:
    assert True
else:
    assert False
try:
    r = socket.if_nameindex([(i, i) for i in range(5)])
except TypeError:
    assert True
else:
    assert False

r = socket.if_nameindex()
assert len(r) == len(r[1]) == 0

r = socket.if_nameindex([(1, 'netdevice1'), (2, 'netdevice2'), (4, 'net
