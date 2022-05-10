import select
# Test select.select()
#
# This test is not very good.  It relies on the user typing something
# at the keyboard.  It would be better to use a pseudo-terminal.
#
# XXX This test is not run by regrtest.py.

import sys
import time

# Create two pipes.
r, w = os.pipe()

# Create a socketpair.
s1, s2 = socket.socketpair()

# Create a file descriptor that will never be ready.
f = os.open(test.test_support.TESTFN, os.O_RDONLY)

# Create a file descriptor that will always be ready.
r, w = os.pipe()
w = os.fdopen(w, 'w')
w.write('x')

# Create a file descriptor that will be ready in one second.
r, w = os.pipe()
w = os.fdopen(w, 'w')

# Do the select.
print 'Doing select() on pipes.'
start = time.time()
r, w, x = select.select([r, s1
