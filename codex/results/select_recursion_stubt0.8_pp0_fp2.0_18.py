import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    f = F()
    try:
        a.append(f)
    except ValueError:
        pass
    else:
        assert 0, "expected ValueError"
    try:
        a.append(f)
    except ValueError:
        pass
    else:
        assert 0, "expected ValueError"


def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            raise ValueError
        fileno = property(fileno)

    f = F()
    try:
        a.append(f)
    except ValueError:
        pass
    else:
        assert 0, "expected ValueError"
    try:
        a.append(f)
    except ValueError:
        pass
    else:
        assert 0, "expected ValueError"


class TestSelect:

    def test_error_conditions(self):
        try:
            select.select([], [], [], "spam")
        except TypeError:
            pass
        else:
            raise Ass
