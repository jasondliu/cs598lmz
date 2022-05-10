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
    time.sleep(1)
    print 'selecting...'
    r, w, x = select.select([s3], [], [], 2)
    print 'select returned'
    print 'r =', r
    print 'w =', w
    print 'x =', x
    if r:
        data = r[0].recv(1024)
        print 'received', `data`
   
