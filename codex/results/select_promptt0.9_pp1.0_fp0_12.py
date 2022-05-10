import select
# Test select.select's edge-triggering behavior on a write end of a pipe.

import select, socket, os

SEND_O_NONBLOCK = os.O_NONBLOCK

READ_SIDE, WRITE_SIDE = os.pipe()
os.set_inheritable(READ_SIDE, True)
os.set_inheritable(WRITE_SIDE, True)

pid = os.fork()
if pid == 0:
    # Child grabs the read end of the pipe, and waits for the select.
    READ_SIDE, WRITE_SIDE = socket.fromfd(READ_SIDE, socket.AF_INET,
                                          socket.SOCK_STREAM), None
else:
    # Parent grabs the write end of the pipe, and spins until he is
    # allowed to write.
    WRITE_SIDE = os.fdopen(WRITE_SIDE, "wb", 0)

rlist, wlist, xlist = [READ_SIDE], [WRITE_SIDE], []
s1, s2 = select.select(rlist, w
