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
