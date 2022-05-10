import select
# Test select.select() with a file descriptor that is -1.
# This should raise an error in the underlying select() call.
# select.select() should raise an OSError.

# http://bugs.python.org/issue13118

try:
    select.select([-1], [], [])
except OSError:
    print('OSError')
else:
    print('no exception')
