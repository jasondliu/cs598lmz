import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 5

    s = select.select([F()], [], [])
    assert a == [1]
    assert s == ([5], [], [])

def test_select_crash():
    # Issue #5173: segfault when a file descriptor is closed during select()
    # with a read event.
    r, w = os.pipe()
    try:
        def close_r():
            os.close(r)
        thread = threading.Thread(target=close_r, args=())
        thread.start()
        # The select should not crash when the read fd is closed while
        # select() is running.
        s = select.select([r], [], [], 1)
        assert s == ([], [], [])
        thread.join()
    finally:
        os.close(w)

