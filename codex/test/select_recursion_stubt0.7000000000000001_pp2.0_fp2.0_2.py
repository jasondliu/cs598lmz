import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    try:
        select.select([F()], [], [])
    except RuntimeError:
        a.append(1)

    try:
        select.select([], [F()], [])
    except RuntimeError:
        a.append(1)

    try:
        select.select([], [], [F()])
    except RuntimeError:
        a.append(1)

    try:
        select.select([F()], [F()], [F()])
    except RuntimeError:
        a.append(1)

    assert a == [1] * 4
