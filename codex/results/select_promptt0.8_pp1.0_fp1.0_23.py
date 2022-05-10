import select
# Test select.select with both a pipe and file descriptors set to pipe
# The select will notify both

import os, select, sys
read_end, write_end = os.pipe()

out_r, out_w = os.pipe()
# make sure we don't get an EINTR
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
if os.fork() == 0:
    # child process
    os.close(read_end)
    os.close(out_w)
    os.write(write_end, "abc")
    os.read(out_r, 4)
    os._exit(1)
else:
    # parent process
    os.close(write_end)
    os.close(out_r)
    l = []
    while True:
        rfd, wfd, efd = select.select([read_end, out_w], [], [])
        if read_end in rfd:
            data = os.read(read_end, 1)
            if not data:
                break
            l
