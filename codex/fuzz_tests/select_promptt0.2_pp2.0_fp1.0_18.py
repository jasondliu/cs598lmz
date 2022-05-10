import select
# Test select.select()

# This is a simple test of select.select()
# It uses select() to wait until data is available to read on stdin
# or until stdin is ready for writing.

# This test is not exhaustive.  It does not test all corner cases.

import sys
import select
import time

if sys.platform[:3] == 'win':
    def test_select():
        print 'This test does not work on Windows'
else:
    def test_select():
        print 'Testing select() on stdin'
        sys.stdout.flush()
        sys.stdin.flush()
        time.sleep(1)
        r, w, x = select.select([sys.stdin], [sys.stdin], [])
        if sys.stdin in r:
            print 'select() says stdin is readable'
        if sys.stdin in w:
            print 'select() says stdin is writable'
        sys.stdout.flush()
        sys.stdin.flush()
        time.sleep(1)
        r, w, x = select
