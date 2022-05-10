import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    import os
    import errno

    print "Testing select() with sockets"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    s.listen(5)
    port = s.getsockname()[1]
    print "listening on port", port

    # We must use the same socket for accepts and connects to
    # trigger the bug.  The connect() must complete before the
    # accept() and the accept() must put us over FD_SETSIZE
    # connections.
    clients = []
    for i in range(FD_SETSIZE):
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(('localhost', port))
        clients.append(c)

    print "accepting connections"
    try:
        while 1:
            r, w, e = select.select([s], [], [])
            if s in r
