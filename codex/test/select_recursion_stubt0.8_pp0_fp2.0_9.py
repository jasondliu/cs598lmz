import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def close(self):
            pass

    f = F()
    t = threading.Thread(target=lambda: a.append(select.select([f], [], [], 2) == ([], [], [])))
    t.start()
    t.join()
    assert a[0]
test_select_mutated()

@pytest.mark.skipif("hasattr(select, 'poll')")
def test_select_bad_file_descriptor():
    # Issue7607: select() should not crash Python when a bad file descriptor
    # is passed
    with pytest.raises(ValueError):
        select.select([-100], [], [])

def test_select_keyboard_interrupt():
    # Issue #27998: select() should not swallow KeyboardInterrupt
    # (except on Windows where it is a no-op)
    if hasattr(signal, 'SIGALRM'):
        signal.signal(signal.SIGALRM, signal.default_int_handler)
