import select
# Test select.select()

def test_select():
    r, w, e = select.select([], [], [], 0)
    assert r == w == e == [], "select returns lists, not tuples"
