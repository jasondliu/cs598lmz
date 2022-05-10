import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    assert select.select([], [], []) == ([], [], [])
    a.append(F())
    try:
        select.select([], [], a, 1)
    except RuntimeError as e:
        assert "list modified during iteration" in str(e)
    else:
        assert 0, "did not raise"
    assert a[0] is F()

def test_select_error():
    a = []

    class F:
        def fileno(self):
            test_select_error()
            return 42
        def close(self):
            a.append("closing")

    a.append(F())
    try:
        # Try to use as much as possible of the select()/poll()
        # codepath, I don't know how to force it.
        os.pipe()
        r, w, x = select.select([], [], a, 1)
    except OSError as e:
        r = w = x = 0
    else:
        assert 0, "did not raise"
