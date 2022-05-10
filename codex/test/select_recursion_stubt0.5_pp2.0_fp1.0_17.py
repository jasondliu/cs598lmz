import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    s = select.select([F(), F()], [], [])
    assert s == ([], [], [])
    s = select.select([F()], [], [])
    assert s == ([], [], [])
    s = select.select([F()], [], [], 0)
    assert s == ([], [], [])

def test_select_keyboardinterrupt():
    # Issue #11853: select() should not swallow KeyboardInterrupt
    import signal
    import threading
    import time
    def run():
        # This function is run in a thread.  It raises a KeyboardInterrupt
        # exception, which should be raised in the main thread.
        time.sleep(1)
        raise KeyboardInterrupt
    thread = threading.Thread(target=run)
    thread.start()
    with pytest.raises(KeyboardInterrupt):
        select.select([], [], [], 2)
    thread.join()

