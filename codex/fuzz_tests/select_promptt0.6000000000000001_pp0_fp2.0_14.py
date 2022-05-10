import select
# Test select.select()
# Test that it can handle all of the different types of file descriptors.

import sys
import os

def test(s, w, x, msg, use_poll=False):
    print >>sys.stderr, '%s ... ' % msg,
    if use_poll:
        r, w, x = select.poll().poll(0)
        r = [f.fd for f in r]
        w = [f.fd for f in w]
        x = [f.fd for f in x]
    else:
        r, w, x = select.select(s, w, x, 0)
    r = [x.fileno() for x in r]
    w = [x.fileno() for x in w]
    x = [x.fileno() for x in x]
    if (r, w, x) == (s, w, x):
        print >>sys.stderr, 'OK'
    else:
        print >>sys.stderr, 'ERROR'
        print >>sys.stderr, 'returned',
