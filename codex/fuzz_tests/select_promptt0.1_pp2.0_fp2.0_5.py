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
        r, w, e = select.select([s1], [s2], [])
        print 'READY', r, w, e
        if r:
            data = s1.recv(1024)
            print 'recv(%d) => %r' % (len(data), data)
        if w:
            s2.send('ping')
            print 'send(4) => ping'
        time.sleep(1)

    s1.close()
    s2.close()

if __name__ == '__main__':
    test_select()
