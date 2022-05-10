import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(0)
    s = select.select([f], [], [], 0.1)
    assert s == ([], [], [])

def test_select_timeout_errno():
    import select
    import errno
    timeout = 0.1
    try:
        select.select([], [], [], timeout)
    except select.error as e:
        assert e.args[0] == errno.EINTR
        assert e.args[1] == "select(timeout=%s)" % timeout
    else:
        py.test.fail("select.error expected")
