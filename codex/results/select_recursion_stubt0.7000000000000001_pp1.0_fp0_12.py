import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([F()], [], [], 0)

def test_select_fds():
    fds = [open("/dev/null")]
    select.select(fds, fds, fds, 0)
    fds[0].close()
    fds[0].close()
    select.select(fds, fds, fds, 0)

def test_select_unhashable():
    a = []
    try:
        select.select([a], [a], [a], None)
    except TypeError:
        pass
    else:
        raise AssertionError("select() unhashable arg did not raise TypeError")
