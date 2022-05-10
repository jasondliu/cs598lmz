import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise OverflowError
        def close(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [], [])
    except Exception:
        pass
    f.close()
    assert a == [1]
