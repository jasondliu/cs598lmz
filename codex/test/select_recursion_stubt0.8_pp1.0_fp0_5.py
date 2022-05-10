import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 7

    assert select.select([F()], [], [], 1) == ([], [], [])
    assert a == [1]


def test_select_non_int():
    class F:
        def fileno(self):
            # returning a float should raise TypeError
            return 1.0

    raises(TypeError, select.select, [F()], [], [], 1)


def test_select_bad_int():
    class F:
        def fileno(self):
            return -1

    raises(ValueError, select.select, [F()], [], [], 1)


class TestSelectTimeout:
    def test_select_timeout(self):
        class X:
            def x():
                return select.select([], [], [], 1)
        assert X.x() == ([], [], [])
