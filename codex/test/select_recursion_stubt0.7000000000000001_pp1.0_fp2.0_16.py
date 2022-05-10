import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return "F"

    select.select([F()], [], [])


def test_select_err():

    class F:
        def fileno(self):
            return "F"

    try:
        select.select([F()], [], [])
    except TypeError as e:
        assert "not a Python file object" in str(e)
    else:
        assert False


class G:
    def fileno(self):
        return "F"


def test_select_err2():
    try:
        select.select([G()], [], [])
    except TypeError as e:
        assert "not a Python file object" in str(e)
    else:
        assert False


def test_select_err3():
    try:
        select.select([], [G()], [])
    except TypeError as e:
        assert "not a Python file object" in str(e)
    else:
        assert False


