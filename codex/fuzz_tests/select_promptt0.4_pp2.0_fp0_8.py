import select
# Test select.select with a timeout

# This test is not very useful, since it doesn't test the timeout
# feature of select.select.  It is included only for completeness.

import select
import time

r, w, x = select.select([], [], [], 0.1)
print r, w, x

start = time.time()
r, w, x = select.select([], [], [], 0.5)
end = time.time()
print r, w, x
print "Elapsed time:", end - start
