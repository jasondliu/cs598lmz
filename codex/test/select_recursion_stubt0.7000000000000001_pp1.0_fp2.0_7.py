import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select(a, a, a)

def test_file_not_closed():
    # Issue 2644.
    # Do not close an arbitrary file descriptor if an exception occurs
    # in select()
    class FileWrapper:
        def __init__(self, fd):
            self.fd = fd
            self.close_called = False

        def fileno(self):
            return self.fd

        def close(self):
            self.close_called = True

    # We can't easily verify that the original fd is not closed.  But
    # we can create a file wrapper with a fileno that is already closed,
    # and verify that it is not closed by select().
    fd = os.open(os.devnull, os.O_RDONLY)
    os.close(fd)
    f = FileWrapper(fd)
    fd_list = [f]
    select.select(fd_list, fd_list, fd_list)
    assert not f.close
