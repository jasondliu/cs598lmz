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
    r, w, x = select.select([s], [], [], 2.0)
    print 'r =', r
    print 'w =', w
    print 'x =', x
    if r:
        conn, addr = s.accept()
        print 'accepted connection from', addr
        data = conn.recv(1024)
        print 'received', `data`
        conn.send('echo:' + data)
        conn.close()
    s.close()

def test_select_timeout():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
