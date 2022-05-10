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
    try:
        r, w, x = select.select([pipe_r], [], [], 0.1)
    except select.error, err:
        if err[0] == 4:
            # interrupted system call
            print "interrupted system call"
        else:
            raise
    else:
        if r:
            print "FAILED: select() returned immediately on empty pipe"
        else:
            print "PASSED"
    sys.exit(0)

else:
    # parent
    os.close(pipe_r)
    os.write(pipe_w, "x
