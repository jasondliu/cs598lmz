import select
# Test select.select() and select.poll() methods.

import os
import sys
import select
import time

# Python seems to have a default limit of 1024 file descriptors.
# We test that poll objects can handle higher numbers than this.
N = 2*1024

test_support.verbose = 1

# Attempt to open all file descriptors.
fds = []
for i in xrange(N):
    try:
        fds.append(os.open("/dev/null", os.O_RDONLY))
    except OSError:
        break

if not fds:
    raise RuntimeError("couldn't open any file descriptors!")

N = len(fds)

if test_support.verbose:
    print "testing with %d file descriptors" % N

# select
def check_select(r, w, x, tv):
    r2, w2, x2 = select.select(r, w, x, tv)
    r2 = list(r2); w2 = list(w2); x2 = list(x2)

