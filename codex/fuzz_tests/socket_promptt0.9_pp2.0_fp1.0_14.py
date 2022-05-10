import socket
# Test socket.if_indextoname and socket.if_nametoindex
# on all interfaces.

def hex_addr(s):
    h = ""
    for c in s:
        h = h + '%02x' % (ord(c),)
    return h
def test_if(name):
    i = socket.if_nametoindex(name)
    print 'if_nametoindex', repr(name), repr(i)
    if i is None or name != socket.if_indextoname(i):
        raise NameError(repr(name))
def test_ifindextoname_error(i):
    try:
        name = socket.if_indextoname(i)
    except socket.error, v:
        if v[0] == errno.EINVAL:
            print 'if_indextoname got expected EINVAL'
        else:
            raise v
    else:
        raise RuntimeError("if_indextoname returns '%s' "
                           "for invalid index '%s'"
                           % (repr(name), repr(i
