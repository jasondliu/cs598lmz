import select
# Test select.select

def test_select():
    import select
    r, w, x = select.select([], [], [])
    assert r == w == x == [], "empty select should return empty lists"
    raises(ValueError, select.select, [], [], [], -1)

def test_select_timeout():
    import select
    import time
    r, w, x = select.select([], [], [], 1)
    assert r == w == x == [], "empty select should return empty lists"
    start = time.time()
    r, w, x = select.select([], [], [], 1)
    stop = time.time()
    assert stop - start < 1.5, "select should return immediately"

def test_select_list():
    import select
    r, w, x = select.select([], [], [], 1)
    assert r == w == x == [], "empty select should return empty lists"
    raises(ValueError, select.select, [None], [], [])

