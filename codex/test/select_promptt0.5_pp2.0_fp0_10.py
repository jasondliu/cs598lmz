import select
# Test select.select for a timeout
import select
import time

rlist, _, _ = select.select([], [], [], 1)
print('rlist is {}'.format(rlist))
print('Elapsed time: {}'.format(time.time() - start))

# Test select.select for a file descriptor
import select
import time

rlist, _, _ = select.select([sys.stdin], [], [], 1)
print('rlist is {}'.format(rlist))
print('Elapsed time: {}'.format(time.time() - start))

# Test select.select for a file descriptor with data ready
import select
import time
import sys

start = time.time()
sys.stdin.write(b'1')
sys.stdin.flush()
rlist, _, _ = select.select([sys.stdin], [], [], 1)
print('rlist is {}'.format(rlist))
print('Elapsed time: {}'.format(time.time() - start))

# Test select.select for a file descriptor with data ready
import select

