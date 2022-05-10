import select
# Test select.select with a bad file descriptor.
# This test is a little bit fragile, but it tests all the interesting
# cases.
import errno
import socket
import sys
L = []
for fd in (-1,
 113041,
 2147483647):
    try:
        select.select([fd], [fd], [fd], 1)
    except ValueError as e:
        L.append(e.args[0])


def bad_fd_list(fds):
    for fd in fds:
        try:
            select.select([fd], [fd], [fd], 1)
        except ValueError as e:
            if e.args[0] not in L:
                print('wrong exception:', e)
            if e.args[0].find('bad file descriptor') == -1:
                print('wrong exception:', e)


bad_fd_list([-1,
 0,
 1,
 2,
 3,
 1048576,
 -2147483648])
if hasattr(select, 'poll'):

    def try_poll_
