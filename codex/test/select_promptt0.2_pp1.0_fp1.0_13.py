import select
# Test select.select()

def test_select():
    import time
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], "select() returned non-empty lists"
    time.sleep(0.2)
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], "select() returned non-empty lists"
    time.sleep(0.2)
    r, w, x = select.select([], [], [], 0.1)
    assert r == w == x == [], "select() returned non-empty lists"

def test_select_timeout():
    import time
    start = time.time()
    select.select([], [], [], 1.0)
    assert time.time() - start >= 1.0, "timeout too short"

def test_select_error():
    try:
        select.select([], [], [], 1.0)
    except select.error:
        pass
    else:
        raise
