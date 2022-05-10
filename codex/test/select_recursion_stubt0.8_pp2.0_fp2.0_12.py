import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    s = [F()]
    try:
        select.select(s, [], [])
    except AttributeError:
        pass
    else:
        assert False
    try:
        select.select([], s, [])
    except AttributeError:
        pass
    else:
        assert False
    try:
        select.select([], [], s)
    except AttributeError:
        pass
    else:
        assert False

if sys.platform == 'win32':
    def test_wait_for_handle():
        # a handle that is always ready
        h = win32event.CreateEvent(None, False, False, None)
        win32event.SetEvent(h)
        try:
            r, w, x = select.select([h], [], [], 0.1)
            assert r == [h], "didn't return the handle"
        finally:
            win32api.CloseHandle(h)


