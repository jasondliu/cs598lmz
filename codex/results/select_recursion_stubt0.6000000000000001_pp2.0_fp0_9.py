import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # not guaranteed to work
            return 0

    f = F()

    try:
        select.select([f], [], [])
    except OSError as e:
        a.append(e)

    try:
        select.select([f], [], [], 1)
    except OSError as e:
        a.append(e)

    assert len(a) == 2, a
    assert a[0].args == a[1].args
