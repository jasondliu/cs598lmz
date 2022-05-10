import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

        def close(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    assert a == []
