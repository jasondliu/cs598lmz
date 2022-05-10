import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    # This used to segfault
    select.select([f], [], [])

def test_select_remove():
    import select
    import socket
    import os

    # Issue #5471: try removing an FD from another thread.
    # Since this test uses a pipe and not a socket, we're not
    # really testing select(), but rather the various internal
    # fd_* data structures which are shared by multiple modules
    # including select.

    r, w = os.pipe()
    t1 = threading.Thread(target=lambda: r)
    t2 = threading.Thread(target=lambda: os.close(w))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def test_select_error():
    import select
    import errno
    import os

    # Issue #11459: if an fd is closed in another thread,
    # select() shouldn't raise an exception (EBADF is ok)
   
