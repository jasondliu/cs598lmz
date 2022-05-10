import select
# Test select.select()

# Create a pair of connected sockets

# Create a pair of connected sockets

def test_select():
    import select
    import socket
    import sys
    import time

    s1, s2 = socket.socketpair()
    s1.setblocking(0)
    s2.setblocking(0)

    for i in range(5):
        print 'BLOCKING'
        r, w, e = select.select([s1], [s2], [], 1.0)
        print 'r =', r
        print 'w =', w
        print 'e =', e
        print 'NON-BLOCKING'
        r, w, e = select.select([s1], [s2], [], 0.0)
        print 'r =', r
        print 'w =', w
        print 'e =', e
        time.sleep(1)

if __name__ == '__main__':
    test_select()
