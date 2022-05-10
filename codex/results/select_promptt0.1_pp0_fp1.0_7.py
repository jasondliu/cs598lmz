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
    r, w, e = select.select([s], [], [], 5.0)
    if s in r:
        print 'got a connection'
        conn, addr = s.accept()
        print 'client address:', addr
        conn.close()
    else:
        print 'timed out, no one connected'
    s.close()

test_select()
