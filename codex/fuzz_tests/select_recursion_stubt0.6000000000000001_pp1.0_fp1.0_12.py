import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except SelectError as err:
        assert err.args == ('filedescriptor out of range in select()',)
    else:
        assert False, "expected SelectError"


def test_select_large_timeout():
    from select import select
    timeout = 1e100
    assert select([], [], [], timeout) == ([], [], [])


def test_select_bad_timeout():
    from select import select
    import errno
    try:
        select([], [], [], -1.0)
    except ValueError as e:
        assert "timeout value must be positive" in str(e)
    else:
        assert False, "expected ValueError"


def test_select_large_fd():
    from select import select
    try:
        select([], [], [], 0, (1 << 32) + 1)
    except ValueError as e:
        assert "microsecond value must be in 0..999999" in
