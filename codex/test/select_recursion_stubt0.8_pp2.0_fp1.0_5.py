import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(42)

    select.select([F()], [], [], 1)

def test_select_mutated_dup():
    a = []

    class F:
        def fileno(self):
            a.append(42)

    r, w, x = select.select([F()], [], [], 0)
    assert len(a) == 1
    r, w, x = select.select([F()], [], [], 0)
    assert len(a) == 2

def test_select_mutated_fd():
    a = []

    class F:
        def fileno(self):
            a.append(42)
            return 3

    a.append(1)
    r, w, x = select.select([F()], [], [], 0)
    assert len(a) == 2
    r, w, x = select.select([F()], [], [], 0)
    assert len(a) == 3

def test_select_mutated_dup_fd():
    a = []

