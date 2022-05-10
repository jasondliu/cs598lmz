import select
# Test select.select()
#
# Test select.select() with a timeout of 0.0.
# This should return immediately, without blocking.

# This test is not very good.  It is possible that select() will
# block for a while, and then return immediately.  This is not
# a bug, but it makes this test fail.

import select
import time

start = time.time()
r, w, x = select.select([], [], [], 0.0)
end = time.time()

if end - start >= 0.5:
    raise RuntimeError("select.select() blocked for %s seconds" % (end - start))

print("OK")
