import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return "not an int"

    with pytest.raises(SelectError):
        select.select([F()], [], [])
    assert a

def test_error_conditions():

    # Issue #7995: select() must check file descriptor conditions
    # before trying the system call.
    with pytest.raises(ValueError):
        select.select([-1], [], [])
    with pytest.raises(TypeError):
        select.select([""], [], [])

    # Issue #8318: select() must check if the timeout is a float
    # and timeout > 0
    with pytest.raises(TypeError):
        select.select([], [], [], "spam")
    with pytest.raises(ValueError):
        select.select([], [], [], -1)
    with pytest.raises(ValueError):
        select.select([], [], [], 0)

def test_windows_specific_errors():
    import errno
    from select import error, poll
