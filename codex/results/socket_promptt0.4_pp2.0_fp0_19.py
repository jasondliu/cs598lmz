import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    socket.if_indextoname(1)
    socket.if_indextoname(1, 'foo')

try:
    socket.if_indextoname(1, 'foo', 'bar')
except TypeError:
    pass
else:
    raise Exception, "if_indextoname() takes at most 3 arguments"

try:
    socket.if_indextoname('foo')
except TypeError:
    pass
else:
    raise Exception, "if_indextoname() takes at most 3 arguments"

try:
    socket.if_indextoname(1, 'foo', 'bar', 'baz')
except TypeError:
    pass
else:
    raise Exception, "if_indextoname() takes at most 3 arguments"

try:
    socket.if_indextoname()
except TypeError:
    pass
else:
    raise Exception, "if_indextoname() takes at most 3 arguments"

# Test socket.if_nametoindex
