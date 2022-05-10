import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [f]

    with pytest.raises(RuntimeError):
        select.select([f], [], [], 0)


def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            return a.pop()
        def close(self):
            pass

    f = F()
    a = [f]

    with pytest.raises(RuntimeError):
        select.select([f], [], [], 0)


def test_select_closed_wait():
    a = []

    class F:
        def fileno(self):
            test_select_closed_wait()
            return a.pop()
        def close(self):
            time.sleep(0.01)

    f = F()
    a = [f]

    with pytest.raises(RuntimeError):
        select.select([f], [], [], 0)


