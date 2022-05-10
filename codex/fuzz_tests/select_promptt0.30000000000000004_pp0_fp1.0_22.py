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
    print 'listening on port %d' % port
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(('localhost', port))
    s3, addr = s.accept()
    s2.send('hello')
    print 'before select'
    r, w, e = select.select([s3], [], [], 1.0)
    print 'after select'
    if s3 in r:
        print 's3 is readable'
        data = s3.recv(1024)
        print 'got %r' % (data,)
    else:
        print 's3 is not readable'
    s2.close()
    s3.close()
    s.
