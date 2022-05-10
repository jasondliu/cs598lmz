import select
# Test select.select()

def test_select():
    import time
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], "select() returned lists, should have been empty"
    time.sleep(0.2)
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], "select() returned lists, should have been empty"
    time.sleep(0.2)
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], "select() returned lists, should have been empty"
    time.sleep(0.2)
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], "select() returned lists, should have been empty"
    time.sleep(0.2)
    r, w, x = select.select([], [], [], 0.1)
