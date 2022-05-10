import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    s.listen(1)
    port = s.getsockname()[1]
    print 'listening on port', port
    r, w, x = select.select([s], [], [], 1.0)
    print 'r', r
    print 'w', w
    print 'x', x
    time.sleep(2)
    r, w, x = select.select([s], [], [], 1.0)
    print 'r', r
    print 'w', w
    print 'x', x
    conn, addr = s.accept()
    print 'accepted', conn, addr
    r, w, x = select.select([s], [], [], 1.0)
    print 'r', r
    print 'w', w
    print 'x', x
    r, w, x = select.select([s
