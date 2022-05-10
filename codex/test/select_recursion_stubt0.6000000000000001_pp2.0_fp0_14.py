import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    select.select([f], a, a, 0)
    f.fileno()

def test_select_closed_exception():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    f.fileno()
    select.select([f], a, a, 0)
    f.fileno()

def test_select_poll():
    p = select.poll()
    p.register(0, select.POLLIN)
    p.poll(0)

def test_select_poll_mutated():
    p = select.poll()

    class F:
        def fileno(self):
            test_select_poll_mutated()
            return 0

    p.register(F(), select.POLLIN)
    p.poll(0)

