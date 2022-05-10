import select
# Test select.select() on a pipe

# This test is a bit of a hack, because we know that the pipe will
# always be ready to read, so we can use a timeout of 0.

import sys
import select
import os

if sys.platform == 'win32':
    import msvcrt

if sys.platform == 'darwin':
    # Skip this test on darwin, because select() doesn't work on pipes.
    # See http://bugs.python.org/issue5154
    raise ImportError

try:
    select.select([sys.stdin], [], [], 0)
except select.error:
    raise ImportError

r, w = os.pipe()

