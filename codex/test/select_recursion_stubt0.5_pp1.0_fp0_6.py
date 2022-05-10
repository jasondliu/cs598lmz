import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def close(self):
            a.append(1)

    try:
        select.select([F()], [], [], 0)
    except:
        pass

    assert a == [1]
