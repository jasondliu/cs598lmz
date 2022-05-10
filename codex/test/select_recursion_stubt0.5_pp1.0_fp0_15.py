import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 0)

def test_select_closed():
    # Issue #11796: select.select() should not raise an exception when
    # a file descriptor is closed during the call.
    r, w = os.pipe()
    os.close(w)

    try:
        select.select([r], [], [], 0)
    finally:
        os.close(r)

def test_select_fd_set_size():
    # Issue #12779: select() should not crash with a file descriptor greater
    # than FD_SETSIZE
    fd = os.dup(1)
    try:
        select.select([fd], [], [], 0)
    finally:
        os.close(fd)
