import select
# Test select.select()
# and select.error

import select
import socket

# XXX Should do a test on unconnected sockets,
# but that doesn't work yet.

# restrict tests to flavors that support select()

if sys.platform[:3] in {'win', 'os2', 'risc'}:
    print("test_select is not supported on", sys.platform)
    sys.exit(0)

def do_select(s, w, x, timeout=None):
    try:
        r,w,x = select.select(s,w,x,timeout)
    except select.error as err:
        errnum = err.args[0]
        if errnum == 0:
            # timeout
            return []
        raise
    return r

def test_select(files):
    do_select((), (), (), 0)
    r,w,x = [], [], []
    if files:
        r,w,x = do_select(files, files, files, timeout=0)
    do_select([], [], [], timeout=0)

