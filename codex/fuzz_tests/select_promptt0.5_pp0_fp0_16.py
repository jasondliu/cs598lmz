import select
# Test select.select

def test_select():
    import select
    # Test that select() returns three empty lists when passed three empty lists
    assert select.select([], [], []) == ([], [], [])
    # Test that it raises a TypeError if passed a non-list
    raises(TypeError, select.select, 0, [], [])
    raises(TypeError, select.select, [], 0, [])
    raises(TypeError, select.select, [], [], 0)
    # Test that it raises a TypeError if passed something which is not a file descriptor
    raises(TypeError, select.select, [0], [], [])
    raises(TypeError, select.select, [], [0], [])
    raises(TypeError, select.select, [], [], [0])
    # Test that it raises a ValueError if passed a negative timeout
    raises(ValueError, select.select, [], [], [], -1)
    # Test that it raises a TypeError if passed something which is not a float or None
    raises(TypeError, select.select, [], [
