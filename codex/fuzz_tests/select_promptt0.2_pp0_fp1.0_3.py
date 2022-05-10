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
    if s in r:
        print 's is readable'
    else:
        print 's is not readable'
    time.sleep(2.0)
    r, w, x = select.select([s], [], [], 1.0)
    if s in r:
        print 's is readable'
    else:
        print 's is not readable'
    conn, addr = s.accept()
    r, w, x = select.select([s], [], [], 1.0)
    if s in r:
        print 's is readable'
    else:
        print 's is not readable
