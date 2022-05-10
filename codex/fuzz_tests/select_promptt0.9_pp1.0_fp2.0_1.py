import select
# Test select.select() with a big timeout.
import time, sys
for i in range(5):
    print "sleeping %d..." % i
    sys.stdout.flush()
    result = select.select([], [], [], (1 << 30) * (1 << 30))
    print "Slept %d seconds and result is %r" % (i, result)
