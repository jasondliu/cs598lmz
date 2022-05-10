import select
# Test select.select()

def test_select():
    # Test basic operation
    r, w, x = select.select([], [], [], 0)
    assert r == w == x == [], "returned lists are not all empty"
    r, w, x = select.select([], [], [], 1)
    assert r == w == x == [], "returned lists are not all empty"

    # Test that it doesn't hang
    r, w, x = select.select([], [], [], 1)
    assert r == w == x == [], "returned lists are not all empty"

    # Test that it does hang
    r, w, x = select.select([], [], [], 10)
    assert r == w == x == [], "returned lists are not all empty"

    # Test that it doesn't hang with a file
    f = open(__file__)
    r, w, x = select.select([f], [f], [f], 1)
    assert r == w == x == [], "returned lists are not all empty"
    f.
