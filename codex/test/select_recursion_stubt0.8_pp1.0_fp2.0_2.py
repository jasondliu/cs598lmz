import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    for i in range(select.PIPE_BUF + 1):
        a.insert(0, i + 1)
        r, _, _ = select.select([F()], [], [], 1)
        assert len(r) == 1

def test_select_keyboardinterrupt():
    def raise_exc():
        raise KeyboardInterrupt

    def raise_exc_after_yield():
        yield
        raise KeyboardInterrupt

    try:
        select.select([], [], [], 0, raise_exc)
    except KeyboardInterrupt:
        pass
    else:
        pytest.fail("expected KeyboardInterrupt")

    try:
        select.select([], [], [], 0, raise_exc_after_yield())
    except KeyboardInterrupt:
        pass
    else:
        pytest.fail("expected KeyboardInterrupt")

def test_select_interrupted_error():
    def raise_interrupted_error():
        raise InterruptedError

    def raise_interrupted_error_after_yield():
        yield
