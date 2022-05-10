import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([], [], [F()], 0)
    a.append(1)
    assert len(a) == 1

def test_select_mutated_with_timeout_zero():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_with_timeout_zero()
            return 0

    select.select([], [], [F()], 0)
    a.append(1)
    assert len(a) == 1
