import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class G:
        def fileno(self):
            a.append(1)
            return 0

    def bad():
        raise ValueError

    select.select([F()], [G()], [], 0)
    raises(ValueError, select.select, [G()], [F()], [], 0)
    raises(ValueError, select.select, [G()], [], [F()], 0)
    raises(ValueError, select.select, [bad()], [], [], 0)
    raises(ValueError, select.select, [], [bad()], [], 0)
    raises(ValueError, select.select, [], [], [bad()], 0)
    assert a == [1]
