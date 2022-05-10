import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    port = s.getsockname()[1]
    print 'listening on port', port
    r, w, x = select.select([s], [], [], 1.0)
    print 'r =', r
    print 'w =', w
    print 'x =', x
    if r:
        conn, addr = s.accept()
        print 'accepted connection from', addr
        conn.close()
    s.close()
    print 'sleeping'
    time.sleep(2.0)
    print 'done'

test_select()
