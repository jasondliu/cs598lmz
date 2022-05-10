import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    print 'Testing if_indextoname()'
    try:
        socket.if_indextoname(1)
    except socket.error, e:
        print 'if_indextoname() not supported'
        return
    print 'if_indextoname() supported'
    try:
        print 'if_indextoname(1) returned', socket.if_indextoname(1)
    except socket.error, e:
        print 'if_indextoname(1) failed:', e

test_if_indextoname()
