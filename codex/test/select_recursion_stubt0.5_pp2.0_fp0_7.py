import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)


def test_select_poll():
    if not hasattr(select, 'poll'):
        skip("test needs select.poll()")

    # Issue #10558: select.poll() should not crash when one of the registered
    # file descriptors gets garbage collected
    class F:
        def fileno(self):
            return 0

    f = F()
    p = select.poll()
    p.register(f)
    del f
    p.poll()


def test_select_with_thread():
    # Issue #15227: select() should not crash when called from a thread
    # different from the main thread
    if not hasattr(select, 'select'):
        skip("test needs select.select()")

    class F:
        def fileno(self):
            return 0

    f = F()
    thread = threading.Thread(target=select.select, args=([f], [], []))
    thread.start()
    thread.join()


