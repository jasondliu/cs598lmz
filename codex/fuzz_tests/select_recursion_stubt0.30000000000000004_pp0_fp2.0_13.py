import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError as e:
        assert str(e) == "I/O operation on closed file."
    else:
        assert False, "expected RuntimeError"

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 1

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError as e:
        assert str(e) == "I/O operation on closed file."
    else:
        assert False, "expected RuntimeError"
