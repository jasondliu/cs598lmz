import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)

    try:
        select.select(a, a, a, 1)
    except RuntimeError as e:
        assert "mutated" in str(e)
    else:
        assert False, "RuntimeError not raised"

def test_select_bad_fd():
    a = []

    class F:
        def fileno(self):
            return -1

    f = F()
    a.append(f)

    try:
        select.select(a, a, a, 1)
    except ValueError as e:
        assert "invalid" in str(e)
    else:
        assert False, "ValueError not raised"

def test_select_bad_fd_2():
    a = []

    class F:
        def fileno(self):
            return 1

    f = F()
    a.append(f)

    try:
        select.select(a, a, a, 1)
    except ValueError as e:
        assert "invalid" in
