import select
# Test select.select with big timeout
import time
print "Testing timeout with 0.5 s"
start = time.time()
s = select.select([], [], [], 0.5)
duration = time.time() - start
print s
print "Duration: %.2f"%duration
print "Testing timeout with 0.1 s"
start = time.time()
s = select.select([], [], [], 0.1)
duration = time.time() - start
print s
print "Duration: %.2f"%duration
