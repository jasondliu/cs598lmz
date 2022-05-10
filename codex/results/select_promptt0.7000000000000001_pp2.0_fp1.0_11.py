import select
# Test select.select() in a way that makes sure it's not blocking.
# For example, a possible implementation of select() on Windows
# might return immediately if the timeout is zero, and the fds
# aren't ready.
#
# This test isn't fast, but it doesn't need to be.

r, w = os.pipe()
r2, w2 = os.pipe()

try:
    timeout = 0.01
    while timeout < 20:
        ready = select.select([r, r2], [], [], timeout)
        if len(ready[0]) == 2:
            break
        timeout *= 2
    else:
        raise TestFailed, "select.select() is blocking"
finally:
    os.close(r)
    os.close(w)
    os.close(r2)
    os.close(w2)

# Issue #2067: select.select raises a ValueError when it was given
# just one argument instead of three.
try:
    select.select([], [], [], None)
except TypeError:
    pass
else:
