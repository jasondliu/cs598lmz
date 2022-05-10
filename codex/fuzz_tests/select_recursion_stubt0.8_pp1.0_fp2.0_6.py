import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    try:
        select.select([F()], [], [])
    except ValueError as exc:
        assert "file descriptor cannot be a negative integer (-1)" == str(exc)
    else:
        assert False, "should raise"

@pytest.mark.skipif("not hasattr(select, 'devpoll')")
def test_devpoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_devpoll_mutated()
            return len(a)

    try:
        select.devpoll(None).register(F())
    except ValueError as exc:
        assert "file descriptor cannot be a negative integer (-1)" == str(exc)
    else:
        assert False, "should raise"

@pytest.mark.skipif("not hasattr(select, 'kqueue')")
def test_kqueue_mutated():
    a = []

    class F:
        def fileno(self):
            test_kqueue_mutated()
            return len(a)
