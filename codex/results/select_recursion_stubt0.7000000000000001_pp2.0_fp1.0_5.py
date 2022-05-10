import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def close(self):
            a.append(1)

    class D:
        def fileno(self):
            return 2

    try:
        s = select.select([F(), D()], [], [])
    except RuntimeError:
        pass

    for f in s[0]:
        pass

    assert a == [1]

def test_issue7127():
    # select.error is not raised anymore, but ValueError is raised instead
    with pytest.raises(ValueError):
        select.select([], [-1], [])
    with pytest.raises(ValueError):
        select.select([], [], [-1])

def test_select_error_str():
    err = select.error(5, "error message")
    assert err.errno == 5
    assert err.strerror == "error message"
    assert str(err) == "[Errno 5] error message"

def test_select_error_repr():
    err = select.error(5, "error message")
    assert err.
