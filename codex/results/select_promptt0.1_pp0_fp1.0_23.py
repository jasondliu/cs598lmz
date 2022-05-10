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
    r, w, e = select.select([s], [], [], 5)
    print 'r =', r
    print 'w =', w
    print 'e =', e
    if s in r:
        conn, addr = s.accept()
        print 'accepted connection from', addr
        conn.close()
    s.close()
    print 'sleeping for 10 seconds...'
    time.sleep(10)
    print 'done'

if __name__ == '__main__':
    test_select()
