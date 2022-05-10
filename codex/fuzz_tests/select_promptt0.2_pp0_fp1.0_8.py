import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    s.setblocking(0)
    port = s.getsockname()[1]
    print 'listening on port', port

    r, w, e = select.select([s], [], [], 5.0)
    if s in r:
        print 'ready for reading'
    else:
        print 'not ready for reading'
    if s in w:
        print 'ready for writing'
    else:
        print 'not ready for writing'
    if s in e:
        print 'ready for exceptions'
    else:
        print 'not ready for exceptions'

    time.sleep(10)
    print 'done'

test_select()
