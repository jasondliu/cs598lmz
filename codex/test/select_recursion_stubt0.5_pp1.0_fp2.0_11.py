import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    def callback():
        a.append(None)
        raise KeyboardInterrupt

    try:
        select.select([F()], [], [], 0.0)
    except KeyboardInterrupt:
        pass
    else:
        assert False, "Should have raised KeyboardInterrupt"

    try:
        select.select([F()], [], [], 0.0, callback)
    except KeyboardInterrupt:
        pass
    else:
        assert False, "Should have raised KeyboardInterrupt"

    assert len(a) == 2
