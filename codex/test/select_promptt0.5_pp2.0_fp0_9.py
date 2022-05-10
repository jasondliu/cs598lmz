import select
# Test select.select

def test_select():
    r, w, e = select.select([1], [2], [3], 1)
    assert r == [1]
    assert w == [2]
    assert e == [3]
    assert r == select.select([1], [2], [3], 1)[0]
    assert w == select.select([1], [2], [3], 1)[1]
    assert e == select.select([1], [2], [3], 1)[2]
    assert r == select.select([1], [2], [3])[0]
    assert w == select.select([1], [2], [3])[1]
    assert e == select.select([1], [2], [3])[2]
    assert r == select.select([1], [2], [3], None)[0]
    assert w == select.select([1], [2], [3], None)[1]
    assert e == select.select([1], [2], [3], None)[2]
