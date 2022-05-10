import select
# Test select.select().

import sys
import time
import select

if sys.version_info[:2] == (2, 6):
    # Python 2.6 added a timeout parameter to select.select.
    TIMEOUT_SUPPORT = True
else:
    TIMEOUT_SUPPORT = False

def test_select():
    fd = sys.stdout.fileno()

    for i in range(5):
        print 'iteration %d' % i
        r, w, x = select.select([fd], [], [], 0.1)
        if r:
            print '\treadable'
        if w:
            print '\twritable'
        if x:
            print '\texceptional'

    # Test whether select.select() supports a timeout.
    if TIMEOUT_SUPPORT:
        print 'select.select() supports a timeout'
    else:
        print 'select.select() does not support a timeout'

    # Without a timeout, this should block indefinitely.
    print 'starting select.select() with no arguments'
    start = time.time()

