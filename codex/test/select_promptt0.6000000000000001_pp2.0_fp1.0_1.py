import select
# Test select.select

def test_select():
    assert select.select([], [], [], 1) == ([], [], [])
    assert select.select([], [], [], -1) == ([], [], [])
    #
    r, w, x = select.select([], [], [], 1)
    assert r == []
    assert w == []
    assert x == []
    #
    r, w, x = select.select([], [], [], -1)
    assert r == []
    assert w == []
    assert x == []
    #
    import sys
    r, w, x = select.select([sys.stdin], [], [], -1)
    assert r == [sys.stdin]
    assert w == []
    assert x == []
    #
    r, w, x = select.select([sys.stdin], [sys.stdout], [], -1)
    assert r == [sys.stdin]
    assert w == [sys.stdout]
    assert x == []
    #
