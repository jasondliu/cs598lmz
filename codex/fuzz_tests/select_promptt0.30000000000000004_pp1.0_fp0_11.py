import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(5)
    s.setblocking(0)
    port = s.getsockname()[1]
    print 'listening on port %d' % port

    # wait for connection
    while True:
        r, w, e = select.select([s], [], [], 1.0)
        if s in r:
            break
        print 'waiting for connection...'

    # connection is ready
    conn, addr = s.accept()
    print 'connection from', addr
    conn.setblocking(0)

    # wait for data
    while True:
        r, w, e = select.select([conn], [], [], 1.0)
        if conn in r:
            break
        print 'waiting for data...'

    # data is ready
    data = conn.recv(1024)

