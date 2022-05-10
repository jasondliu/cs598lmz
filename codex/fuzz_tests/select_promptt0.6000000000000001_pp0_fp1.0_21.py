import select
# Test select.select with a file descriptor that is not a socket.
import os
import sys

r, w = os.pipe()

try:
    select.select([r], [], [])
except ValueError:
    print('ValueError')
else:
    print('no ValueError')
