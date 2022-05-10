import socket
# Test socket.if_indextoname()

def test(family, address, expected):
    print 'socket.if_indextoname(%r, %r)' % (family, address)
    try:
        result = socket.if_indextoname(family, address)
    except socket.error, err:
        print 'Error:', err
    else:
        print 'Result:', result
        if result != expected:
            print 'Expected:', expected

test(socket.AF_INET, 0, 'lo')
test(socket.AF_INET, 1, 'eth0')
test(socket.AF_INET, 2, 'eth1')
test(socket.AF_INET, 3, 'eth2')
test(socket.AF_INET, 4, 'eth3')
test(socket.AF_INET, 5, 'eth4')
test(socket.AF_INET, 6, 'eth5')
test(socket.AF_INET, 7, 'eth6')
test(socket.AF_INET, 8, 'eth7')
test(socket.AF_IN
