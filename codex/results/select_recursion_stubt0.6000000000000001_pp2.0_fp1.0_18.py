import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    select.select([F()], [], [])

def test_select_error():
    select.select([1], [], [], 0)

def test_select_empty():
    select.select([], [], [], 0)

def test_select_timeout():
    select.select([], [], [], 0.5)
    select.select([], [], [], 0)
    select.select([], [], [], None)

def test_select_read():
    r, w, x = select.select([], [], [], 0)
    assert r == []
    assert w == []
    assert x == []
    r, w, x = select.select([sys.stdin], [], [], 0)
    assert r == []
    assert w == []
    assert x == []

def test_select_write():
    r, w, x = select.select([], [], [], 0)
    assert r == []
    assert w == []
    assert x == []
    r, w, x
