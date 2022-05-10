import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    # On Windows, the fd of a socket is a small integer,
    # which is also the index of the list element.
    rlist = [object() for x in range(100)]
    rlist[1] = F()
    rlist, wlist, xlist = select.select(rlist, [], [], 0)
    assert not rlist
    assert not wlist
    assert not xlist
    assert len(rlist) == 100

def test_select_mutated_2():
    # On Unix, the fd of a socket is a file descriptor,
    # which is not necessarily the index of the list element.
    a = []

    class F:
        def fileno(self):
            return a[0]

    rlist = [F() for x in range(100)]
    a.append(1)
    rlist, wlist, xlist = select.select(rlist, [], [], 0)
    assert not rlist
    assert not wlist
    assert not xlist
    assert len(rlist) == 100
