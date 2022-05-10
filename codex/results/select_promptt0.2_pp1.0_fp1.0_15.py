import select
# Test select.select()

# This is a simple test of select.select().
# It uses select() to wait until stdin is ready,
# then reads a line and exits.

# This is a simple test of select.select().
# It uses select() to wait until stdin is ready,
# then reads a line and exits.

import select
import sys

print 'starting'

while True:
    iwtd, owtd, ewtd = select.select([sys.stdin], [], [], 1.0)
    if iwtd:
        line = sys.stdin.readline()
        print 'read line:', line
        break
    else:
        print 'waiting for ready'

print 'exiting'
