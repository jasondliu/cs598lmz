import socket
# Test socket.if_indextoname()

# Test with a valid interface index
ifname = socket.if_indextoname(1)
if ifname != 'lo':
    print('if_indextoname(1) returned %s, expected lo' % repr(ifname))

# Test with an invalid interface index
try:
    socket.if_indextoname(9999999)
except OSError as e:
    if e.errno == errno.EINVAL:
        print('Correctly raised EINVAL')
    else:
        raise

# Test with an invalid argument
try:
    socket.if_indextoname('foo')
except TypeError:
    print('Correctly raised TypeError')
