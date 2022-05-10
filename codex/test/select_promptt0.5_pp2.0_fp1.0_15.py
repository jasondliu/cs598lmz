import select
# Test select.select() for a timeout (as opposed to just blocking)

def test_select_timeout():
    r, w, x = select.select([], [], [], 1)
    assert r == w == x == [], "empty select should return empty lists"
