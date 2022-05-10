import select
# Test select.select()

import socket

def test_select():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    s.listen(1)
    s.setblocking(0)
    port = s.getsockname()[1]
    print 'listening on port', port
    r, w, e = select.select([s], [], [], 1.0)
    if s in r:
        print 'ready for reading'
    else:
        print 'not ready for reading'
    s.close()

test_select()
