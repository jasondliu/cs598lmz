import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

        def close(self):
            a.append(1)

    s = select.select([F()], [], [])
    del s
    gc.collect()

def f():
    for i in range(10000):
        yield i

def test_select_mutated2():
    a = 0
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    class F:
        def fileno(self):
            fd.close()
            return sys.maxsize

        def close(self):
            nonlocal a
            a += 1

    s = select.select([F()], [], [])
    del s
    gc.collect()
    assert a == 1

def test_select_unhashable():
    class F:
        def fileno(self):
            return sys.maxsize

    s = select.select([F()], [], [])
    del s
    gc.collect()

