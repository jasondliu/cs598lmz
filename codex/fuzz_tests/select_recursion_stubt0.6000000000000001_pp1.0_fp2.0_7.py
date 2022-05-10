import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select(a, [], [])
    except ValueError as e:
        assert str(e) == 'filedescriptor out of range in select()'
    except RuntimeError as e:
        assert str(e) == 'maximum recursion depth exceeded'
    else:
        assert False, "expected ValueError or RuntimeError"


def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.pop(0)
            return 0

    a.append(F())
    try:
        select.select(a, [], [])
    except ValueError as e:
        assert str(e) == 'I/O operation on closed file'
    except RuntimeError as e:
        assert str(e) == 'maximum recursion depth exceeded'
    else:
        assert False, "expected ValueError or RuntimeError"


class LongerThanFifteen:
    def fileno(self):
        return 0

def test
