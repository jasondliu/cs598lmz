import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def close(self):
            a.append(1)

    f = F()
    fd = f.fileno()
    try:
        select.select([fd], [], [])
    except RuntimeError:
        pass
    f.close()
    assert a == [1]
