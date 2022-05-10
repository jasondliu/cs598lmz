import socket
# Test socket.if_indextoname()

def test(ind, name):
    if socket.if_indextoname(ind) != name:
        raise ValueError("if_indextoname(%d) should be %s, not %s" %
                         (ind, name, socket.if_indextoname(ind)))

if_indextoname = socket.if_indextoname

if __name__ == '__main__':
    test(1, 'lo0')
    test(2, 'gif0')
    test(3, 'stf0')
    test(4, 'en0')
    test(5, 'en1')
    test(6, 'fw0')
    test(7, 'en2')
    test(8, 'en3')
    test(9, 'p2p0')
    test(10, 'en4')
    test(11, 'bridge0')
    test(12, 'en5')
    test(13, 'utun0')
    test(14, 'utun1')
