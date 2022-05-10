import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket()
    s.setblocking(False)
    s.bind(('', 0))
    s.listen(5)
    port = s.getsockname()[1]
    print('listening on port %d' % port)

    r, w, e = select.select([s], [], [], 5)
    print('r = %s, w = %s, e = %s' % (r, w, e))

    c = socket.socket()
    c.connect(('localhost', port))
    c.send(b'hello')
    c.close()

    r, w, e = select.select([s], [], [], 5)
    print('r = %s, w = %s, e = %s' % (r, w, e))

    r, w, e = select.select([s], [], [], 5)
