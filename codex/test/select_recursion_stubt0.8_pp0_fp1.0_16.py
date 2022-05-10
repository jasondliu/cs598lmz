import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 2

        def close(self):
            a.append(1)

    class G:
        def fileno(self):
            return 3

        def close(self):
            a.append(2)

    # Create a bunch of file descriptors
    fds = [F(), G(), sys.stdin, sys.stdout]

    # poll them
    r, w, x = select.select(fds, fds, fds)

    # close them
    for fd in r+w+x:
        fd.close()

    assert a == [1, 2], a

    class BadFile:
        def fileno(self):
            return 4

