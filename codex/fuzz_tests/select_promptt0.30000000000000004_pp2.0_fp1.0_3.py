import select
# Test select.select

def test_select():
    import select

    # Test that select() works with an empty list.
    select.select([], [], [])

    # Test select() with a file descriptor that is too large.
    # This should raise an exception.
    try:
        select.select([], [], [], 1.0, 1 << 100)
    except ValueError:
        pass
    else:
        raise TestFailed, "expected exception not raised"

    # Test select() with a negative timeout.
    # This should raise an exception.
    try:
        select.select([], [], [], -1.0)
    except ValueError:
        pass
    else:
        raise TestFailed, "expected exception not raised"

    # Test select() with a non-integer timeout.
    # This should raise an exception.
    try:
        select.select([], [], [], 1.0)
    except ValueError:
        pass
    else:
        raise TestFailed, "expected exception not raised"

    # Test select() with a non-numeric timeout.
