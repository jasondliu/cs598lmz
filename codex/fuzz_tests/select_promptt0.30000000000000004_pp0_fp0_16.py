import select
# Test select.select()

def test_select():
    """
    Test select.select()
    """
    print 'Testing select.select()'
    r, w, x = select.select([], [], [], 0)
    assert r == []
    assert w == []
    assert x == []
    r, w, x = select.select([], [], [], 0.0)
    assert r == []
    assert w == []
    assert x == []
    r, w, x = select.select([], [], [], 0.1)
    assert r == []
    assert w == []
    assert x == []
    r, w, x = select.select([], [], [], 1.0)
    assert r == []
    assert w == []
    assert x == []
    r, w, x = select.select([], [], [], 1.1)
    assert r == []
    assert w == []
    assert x == []
    r, w, x = select.select([], [], [], 10.0)
    assert r == []
    assert w
