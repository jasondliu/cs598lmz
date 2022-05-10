import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del a[:]
            return 5

    cs = [F()]
    css = list(cs)
    select.select(cs, cs, cs)
    assert css == cs == []


def test_select_closed():
    fds = []
    for i in range(4):
        r, w = os.pipe()
        fds.extend([r, w])

    r, _, _ = select.select(fds, [], [], 0)
    assert r == []

    os.close(fds[2])
    r, _, _ = select.select(fds, [], [], 0)
    assert r == []

    os.close(fds[1])
    r, _, _ = select.select(fds, [], [], 0)
    assert r == [fds[0]]
    os.close(fds[0])

    r, _, _ = select.select(fds, [], [], 0)
    assert r == [fds[3]]
