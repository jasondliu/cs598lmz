import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop(0)

    class G:
        def fileno(self):
            return a.pop(0)

    a = [4, 3]
    for fd_set, count in [([F(), G()], 1), ([F(), F()], 0)]:
        if sys.platform == 'win32':
            # select() under Windows should not crash even if a file
            # descriptor is mutated
            r, w, x = select.select(fd_set, fd_set, fd_set, 1)
        else:
            # select() under Unix should raise a ValueError if a file
            # descriptor is mutated
            try:
                r, w, x = select.select(fd_set, fd_set, fd_set, 1)
            except ValueError:
                pass
            else:
                assert 0, 'expected ValueError'

        print("for fd_set %r: got %d fds ready" % (fd_set, len(r)+len(w)+len(x)))
        if sys.platform == 'win32':
