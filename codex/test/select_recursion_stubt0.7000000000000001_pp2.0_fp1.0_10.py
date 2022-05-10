import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def mutate(lst):
        yield 3
        lst.append(F())

    p = mp.Pool(1)
    lst = []
    for i in p.imap_unordered(mutate, [lst]):
        pass
    p.close()
    p.join()

def test_select_large_timeout():
    # Issue #8152: select() should handle large timeouts
    r, w = mp.Pipe(duplex=False)
    t = time.monotonic()
    sel = select.select([r], [], [], 3.14159265)
    t = time.monotonic() - t
    assert 0.1 < t < 3.2, t
    assert not sel[0], sel[0]

def test_worker_failure():
    # Issue #8206: the initializer should not be called if the worker fails to
    # start
    class TestException(Exception):
        pass
    def init():
        raise TestException()
    pool = mp
