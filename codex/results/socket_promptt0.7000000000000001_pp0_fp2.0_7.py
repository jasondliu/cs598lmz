import socket
# Test socket.if_indextoname()

def test(ifname, ifindex):
    try:
        name = socket.if_indextoname(ifindex)
    except socket.error, e:
        print 'if_indextoname(%d) failed: %s' % (ifindex, repr(e))
    else:
        print 'if_indextoname(%d) returned %s, expected %s' % (ifindex,
          repr(name), repr(ifname))
        if name != ifname:
            print 'WARNING: did not return expected name!'

test('lo', 1)
test('eth0', 2)
test('eth1', 3)
test('eth2', 4)
print 'Trying to pass an invalid index...'
test('lo', 0)
test('lo', -1)
test('lo', 5)
test('lo', 123456)
test('lo', 8000000000000)
print 'Trying to pass an invalid type...'
try:
    socket.if_indextoname(None)
except TypeError:
    print 'if_indext
