import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], a, a, 0)

def test_select_invalid_fd():
    a = []
    try:
        select.select([1], a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_invalid_timeout():
    a = []
    try:
        select.select([], a, a, -1)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_bad_parameters():
    a = []
    try:
        select.select([], a, a, 0, 1)
    except TypeError:
        pass
    else:
        assert False, "expected TypeError"

def test_select_bad_parameters2():
    a = []
    try:
        select.select([], a, a, 0, None, 1)
    except TypeError:
        pass
    else:
        assert False, "expected TypeError
