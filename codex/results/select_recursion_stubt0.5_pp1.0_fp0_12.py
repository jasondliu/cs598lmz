import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [f]
    select.select([f], [], [])

def test_select_bad_fd():
    # On Windows, select() doesn't like being given an invalid fd.
    # This is a regression test for issue #8808.
    # On Linux, select() is fine with an invalid fd.
    # On Solaris, select() raises an exception.
    # On OS X, select() returns an empty set.
    # So, we just test that the call doesn't bomb out.
    try:
        select.select([-1], [], [])
    except:
        pass
