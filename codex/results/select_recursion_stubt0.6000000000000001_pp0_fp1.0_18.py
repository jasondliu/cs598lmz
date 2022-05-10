import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    def f():
        return F()

    select.select([f()], [], [])
    assert a == [1]

def test_select_closed_fd():
    class F:
        def fileno(self):
            return 1

    f = F()
    import os
    os.close(1)
    try:
        f.fileno()
    except OSError:
        return
    py.test.fail("did not raise")

def test_select_closed_fd2():
    import os
    fd = os.pipe()[0]
    os.close(fd)
    try:
        select.select([fd], [], [])
        py.test.fail("did not raise")
    except ValueError:
        pass

def test_select_closed_fd3():
    import os
    fd = os.pipe()[0]
    os.close(fd)
    try:
        select.select([fd], [fd], [fd])
        py.test.fail("did
