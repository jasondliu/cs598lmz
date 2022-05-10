import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def close(self):
            a.append(1)

    rlist = [F(), F()]
    wlist = [F(), F()]
    xlist = [F(), F()]

    select.select(rlist, wlist, xlist)

    for f in rlist + wlist + xlist:
        f.close()

    assert a == [1,1,1,1,1,1]
