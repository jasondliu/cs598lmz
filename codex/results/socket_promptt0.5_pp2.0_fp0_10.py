import socket
# Test socket.if_indextoname (was missing in Python 2.7, see #17079)
socket.if_indextoname(1)

# Issue #11395: test that os.get_inheritable and os.set_inheritable
# raise a ValueError when the fd is closed
import os
fd = os.open(os.devnull, os.O_RDONLY)
os.close(fd)
try:
    os.get_inheritable(fd)
except ValueError:
    pass
else:
    print("expected ValueError from os.get_inheritable()")
try:
    os.set_inheritable(fd, True)
except ValueError:
    pass
else:
    print("expected ValueError from os.set_inheritable()")

# Issue #11110: test that os.stat_float_times() can be called
import os
os.stat_float_times(False)
os.stat_float_times(True)

# Issue #7473: test that the pwd module is working
import pwd
pwd.getpw
