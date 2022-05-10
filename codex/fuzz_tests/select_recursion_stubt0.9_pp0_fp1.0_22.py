import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    def g():
        select.select(a, a, a)
    for i in range(10):
        assert_raises(TypeError, g)

def test_select_closed_parameter():
    rlist = [open(__file__, 'rb'), None]
    wlist = rlist
    xlist = rlist
    timeout = 30.0
    rlist[0].close()
    rfd, wfd, xfd = select.select(rlist, wlist, xlist, timeout)

    # select() returns the open fileno() in each list
    assert rfd == [rlist[-1]]
    assert wfd == [wlist[-1]]
    assert xfd == [xlist[-1]]
