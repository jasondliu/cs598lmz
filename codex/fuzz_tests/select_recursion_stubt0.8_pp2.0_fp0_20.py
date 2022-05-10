import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    a.append(0)

    try:
        select.select([f], [], [], 0)
    except RuntimeError:
        pass

def test_wakeup():
    import select

    r, _w, _x = select.select([], [], [], 0.1)
    assert not r, r

    r, _w, _x = select.select([], [], [], 0)
    assert not r, r

def test_error():
    import select

    f = open(__file__)
    try:
        select.select([], [], [], 0)
    except ValueError as e:
        assert str(e).startswith("filedescriptor out of range")

    try:
        select.select([f], [], [], 0)
    finally:
        f.close()
