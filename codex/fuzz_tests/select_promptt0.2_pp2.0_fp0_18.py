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
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(('localhost', port))
    s3, addr = s.accept()
    print 'accepted from', addr
    s2.send('hello')
    print 'hello sent'
    for i in range(5):
        print i
        r, w, e = select.select([s3], [], [], 1)
        if s3 in r:
            print repr(s3.recv(100))
        else:
            print 'timed out'
    s3.close()
    s2.close()
    s.close()

test_select()
