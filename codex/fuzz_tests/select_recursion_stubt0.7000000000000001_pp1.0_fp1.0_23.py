import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4

    select.select([F()], [], [])
    del a[:]

def test_select_err():
    a = []

    class F:
        def fileno(self):
            return 4

    try:
        select.select([], [], [F()])
    except OSError, e:
        assert e.errno == 9
        assert e.strerror == "Bad file descriptor"
    else:
        assert 0, "OSError should have been raised"

    del a[:]

def test_select_large():
    # Issue #10234: select() must not return negative file descriptors
    # when the list of parameters contains more than 2048 items.
    a = []
    l = range(2049)
    r = select.select(l, l, l)
    del a[:]
    assert r == ([], [], [])

def test_select_large_2():
    # Issue #10234: select() must not return negative file descriptors
    # when the list of parameters contains more than 2048 items.

