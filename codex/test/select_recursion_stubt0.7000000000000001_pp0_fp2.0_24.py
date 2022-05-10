import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    def f():
        a.append(1)
        raise KeyboardInterrupt
    try:
        select.select([f()], [], [])
    except KeyboardInterrupt:
        pass
    assert a == [1]
    try:
        select.select([F()], [], [])
    except RuntimeError:
        pass
    try:
        select.select([f()], [f()], [f()])
    except KeyboardInterrupt:
        pass
    assert a == [1, 1, 1, 1]
    a[:] = []
    try:
        select.select([F()], [], [])
    except RuntimeError:
        pass

def test_select_keyboardinterrupt_2():
    import select, os
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == []

def test_select_keyboardinterrupt_3():
    import select, os
    r, w, x = select.select([], [], [], 1.1)
