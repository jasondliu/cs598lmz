import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    res = select.select([], a, [])

    # Fileno of the original object should be preserved.
    assert a[0].fileno() == 0

def test_select_mutated_timeout():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    res = select.select([], a, [], timeout=1)

    # Fileno of the original object should be preserved.
    assert a[0].fileno() == 0


def test_select_mutated_closed():
    a = []

    class F:
        def __init__(self):
            self.closed = False

        def close(self):
            self.closed = True

        def fileno(self):
            if self.closed:
                raise ValueError("I/O operation on closed file.")

            test_select_mutated_closed()
            return 0

    f = F()
    a.append(f)
   
