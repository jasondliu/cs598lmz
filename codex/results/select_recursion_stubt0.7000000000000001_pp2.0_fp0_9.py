import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return f.fileno()

    f = F()
    select.select([f], [], [], 0.1)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            f.close()
            return f.fileno()

    f = F()
    select.select([f], [], [], 0.1)
    # in the new world, we would have a.append(2) just
    # before the f.close() call, but not anymore...
    assert a == [1]

def test_poll_mutated():
    a = []
    pollster = select.poll()

    class F:
        def fileno(self):
            test_poll_mutated()
            return f.fileno()

    f = F()
    pollster.register(f, select.POLLIN)
    pollster.poll(0.1)

def test_poll_closed():
    a = []
    pollster = select.poll()

    class F
