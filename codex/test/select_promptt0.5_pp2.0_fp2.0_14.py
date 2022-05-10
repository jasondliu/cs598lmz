import select
# Test select.select() for reading from an open file descriptor
# (stdin in this case).
# This is a simple test of select.select() for reading from an open file
# descriptor (stdin in this case).
# This is written as a separate test because it is not possible to
# test select.select() using a subprocess and the -u command line
# option.
import select
import sys
import time
print('Please type something on stdin within 10 seconds...')
r, w, x = select.select([sys.stdin], [], [], 10)
if r:
    s = sys.stdin.readline()
    print('You typed:', s)
else:
    print('You did not type anything!')
