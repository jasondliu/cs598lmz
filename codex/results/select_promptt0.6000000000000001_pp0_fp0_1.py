import select
# Test select.select().
#
# Test that select.select() returns descriptors that are ready for
# I/O, and that those descriptors have appropriate bits set in the
# returned select.select() mask.
#
# This test is Linux specific; it uses Linux specific /proc/self/fd
# files to determine the number of open descriptors.

import os, select, sys, time
from test import test_support

if sys.platform != "linux2":
    test_support.verbose = 0
    print "This test is Linux specific; skipping."
    sys.exit(0)

# Figure out how many file descriptors to use.
fd_dir = "/proc/self/fd"
fd_count = 0
while True:
    fd_name = "%s/%d" % (fd_dir, fd_count)
    if not os.path.exists(fd_name):
        break
    fd_count += 1

# Make sure test isn't bogus.
if fd_count < 3:
    print "this test is bogus; fd_count is %d"
