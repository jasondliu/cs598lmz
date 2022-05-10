import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    select.select([F()], [], [], 0)
    select.select([a], [], [], 0)
    raises(ValueError, select.select, [a], [], [], 0)

def test_select_closed_fd():
    import os, errno
    fds = [os.open('/dev/null', os.O_RDONLY) for i in range(3)]
