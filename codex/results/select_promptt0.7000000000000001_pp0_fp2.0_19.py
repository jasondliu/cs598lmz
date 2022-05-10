import select
# Test select.select() on a socket, blocking
# and non-blocking.

import socket

from test_support import verbose

def test(family=socket.AF_INET, socktype=socket.SOCK_STREAM):
    if verbose:
        print '\nTesting socket with family', family, 'and type', socktype
    s = socket.socket(family, socktype)
    try:
        msg = 'This is a test'
        s.setblocking(0)
        s.connect(('localhost', 80))
        # Should be writable immediately
        r,w,e = select.select([], [s], [], 1)
        if s not in w:
            print 'socket not immediately writable'
        else:
            s.send(msg)

        r,w,e = select.select([s], [], [], 1)
        if s not in r:
            print 'socket not readable'
        else:
            got = s.recv(len(msg))
            if got != msg:
                print 'incorrect data received'

        s.set
