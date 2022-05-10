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
    r, w, e = select.select([s], [], [], 1.0)
    if s in r:
        print 's is readable'
    else:
        print 's is not readable'
    conn, addr = s.accept()
    print 'accepted connection from', addr
    r, w, e = select.select([s], [], [], 1.0)
    if s in r:
        print 's is readable'
    else:
        print 's is not readable'
    conn.close()
    s.close()

# test_select()

# Test select.poll()

def test_poll():
    import select
    import socket
    import time
    s
