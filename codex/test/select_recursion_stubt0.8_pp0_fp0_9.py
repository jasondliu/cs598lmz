import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
        def close(self):
            pass

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except AttributeError:
        return

    assert 0, "didn't raise AttributeError"

def test_select_closed():
    fd = os.open(__file__, os.O_RDONLY)
    try:
        f = open(__file__, "rb")
        fd2 = f.fileno()
        try:
            os.close(fd2)
            a = select.select([f], [], [])
        finally:
            f.close()
        assert a == ([], [], []), a
    finally:
        os.close(fd)

def test_select_interrupted_error():
    f = open(__file__, "rb")
    fd = f.fileno()
    class FakeSignal:
        @classmethod
        def signal(cls, a, b):
            raise Exception
