import select
# Test select.select()

def test_select():
    # Test select() with an empty list
    r, w, x = select.select([], [], [], 1)
    assert len(r) == 0, "empty read list should return immediately"
    assert len(w) == 0, "empty write list should return immediately"
    assert len(x) == 0, "empty exception list should return immediately"

    # Test select() with a list containing only one element
    r, w, x = select.select([sys.stdin], [], [], 1)
    assert len(r) == 1, "read list with one element should return immediately"
    assert len(w) == 0, "write list should return immediately"
    assert len(x) == 0, "exception list should return immediately"

    # Test select() with a list containing more than one element
    r, w, x = select.select([sys.stdin, sys.stdout], [], [], 1)
    assert len(r) == 2, "read list with two elements should return immediately"
    assert len(w) == 0, "
