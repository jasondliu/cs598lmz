import select
# Test select.select() on a pipe
#
# select() should return immediately when there is no data to read.
#
# This test will fail if there is a bug in select() and it waits
# for a timeout before returning.  The child process will then
# be killed by the test harness.

import os, select, sys

pipe_r, pipe_w = os.pipe()

pid = os.fork()
if pid == 0:
    # child
    os.close(pipe_w)
