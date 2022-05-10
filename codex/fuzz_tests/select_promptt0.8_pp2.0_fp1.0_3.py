import select
# Test select.select() by selecting only stdin.
[i,o,e] = select.select([sys.stdin],[],[],0.0)
# If input is waiting, read it.
if (i):
    print 'Reading stdin...'
    input = sys.stdin.readline().strip()
else:
    print 'no input'

import sys
import select
# Test select.select() by selecting only stdin.
[i,o,e] = select.select([sys.stdin],[],[],0.0)
# If input is waiting, read it.
if (i):
    print 'Reading stdin...'
    input = sys.stdin.readline().strip()
else:
    print 'no input'

import sys
import select
# Test select.select() by selecting only stdin.
[i,o,e] = select.select([sys.stdin],[],[],0.0)
# If input is waiting, read it.
if (i):
    print 'Reading stdin...'
    input = sys.stdin.readline().strip()
else
