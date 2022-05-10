import select
# Test select.select, which is not a system call.
select.select([], [], [], 1)

# Test a couple of system calls that are not exposed by the posix module,
# but are exposed by the C lib.

import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetStdHandle(-12)
else:
    from ctypes import CDLL, c_int, c_void_p
    libc = CDLL("libc.so.6")
    libc.getpgrp()
    libc.tcgetpgrp(c_int(0))
