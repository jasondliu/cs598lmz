import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    r, w, x = select.select([F()], [], [])
    a.append(r)
    a.append(w)
    a.append(x)
    assert a == [], a

    r, w, x = select.select([], [F()], [])
    a.append(r)
    a.append(w)
    a.append(x)
    assert a == [], a

    r, w, x = select.select([], [], [F()])
    a.append(r)
    a.append(w)
    a.append(x)
    assert a == [], a
