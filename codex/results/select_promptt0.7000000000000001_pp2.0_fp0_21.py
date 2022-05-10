import select
# Test select.select() with a timeout.

# This test should be used together with test_poll.
# It should be run after test_poll.

from select import *
from test import test_support
import time, os

searcher = test_support.findfile("start.txt", subdir="select-tests")

timeout = 1

print "Creating start.txt ..."
f = open(searcher, 'w')
f.write('start')
f.close()

print "select(rlist, wlist, xlist, timeout) ..."
r, w, x = select([], [], [], timeout)
print "->", r, w, x

print "Waiting for reader to finish ..."
f = open(searcher, 'r')
while f.read(1) != 's':
    print "  -> waiting for reader to finish"
    time.sleep(1)
f.close()
os.unlink(searcher)

print "Waiting for the timeout ..."
time.sleep(timeout)
r, w, x = select([], [], [],
