import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    class F2:
        def fileno(self):
            a.append(1)
            return 1

    try:
        select.select([F()], [F()], [F()], 0.0)
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"
    try:
        select.select([F2()], [F2()], [F2()], 0.0)
    except ValueError:
        assert False, "ValueError raised"
    assert a, "ValueError raised too early"

class F(object):
    def fileno(self):
        return 1

def test_select_with_object():
    # Issue #8361: select() should not raise a TypeError when given
    # an object which has a fileno() method
    select.select([F()], [F()], [F()], 0.0)


def test_select_str():
    # Issue #13051: select() should not raise a TypeError when given
    # a str for any of the arguments.

