import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            del a[:]

    select.select([F()], [], [], 0)

def test_select_closed_fileno():
    a = []
    class F:
        closed = False
        def fileno(self):
            if self.closed:
                raise ValueError("I'm closed")
            return 0
        def close(self):
            self.closed = True

    f = F()
    select.select([f], [], [], 0)
    f.close()
    select.select([f], [], [], 0)
