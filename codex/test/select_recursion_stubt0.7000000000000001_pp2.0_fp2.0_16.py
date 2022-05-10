import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()

    def g():
        a.append(1)
        select.select([f], [], [])
    th = threading.Thread(target=g)
    th.daemon = True
    th.start()
    time.sleep(.5)
    test_support.gc_collect()
    th.join()

def test_select_wait():
    # Issue #17650: select() should work in Windows without a timeout
    # and without any file handles.
    with warnings.catch_warnings(record=True) as ws:
        warnings.simplefilter('error', DeprecationWarning)
        select.select([], [], [])
        assert not ws, ws

if __name__ == '__main__':
    test_main()
