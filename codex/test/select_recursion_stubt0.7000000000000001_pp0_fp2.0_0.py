import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

        def close(self):
            a.append(1)

    f = F()
    f.close()
    f.fileno()
    f.fileno()
    f.fileno()
    f.fileno()

    for i in range(1024):
        r = [f]
        ret = select.select(r, [], [])
        assert ret == ([f], [], [])
