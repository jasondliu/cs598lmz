import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return F.fd

        def close(self):
            a.append(1)

    F.fd = select.pipe()[1]

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

    F.fd = F.fd.fileno()
    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

    F.fd = 1
    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

    F.fd = None
    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

def test_select_exception():
    class F:
        def fileno(self):
            raise Exception

        def close(self):
            raise Exception
