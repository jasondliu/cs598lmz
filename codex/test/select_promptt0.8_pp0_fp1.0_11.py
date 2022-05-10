import select
# Test select.select()
# This is to see whether select() returns immediately when there is
# nothing to read or when timeval is zero.
#
# This test is used rather than actually checking the code because
# Brad's code is non-deterministic and would require a far more complex
# test case if we were to actually test whether it did what we expected.
#
# The test output should be run in the background and then Ctrl-C
# interrupted.  The output will then be examined to assess whether the
# select() calls are correctly returning immediately.
import select
import time
import sys

RD_FD = 1

timeval = 0,0
for i in xrange(100000):
    print >> sys.stderr, i
