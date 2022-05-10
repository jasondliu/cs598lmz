import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [], 0.1)
    test_select_mutated()
    a.append(1)
    select.select([], [F()], [], 0.1)
    test_select_mutated()
    a.append(2)
    select.select([], [], [F()], 0.1)
    test_select_mutated()
    a.append(3)

def test_select_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            return len(a)

    try:
        select.select([F()], [], [], 0.1)
    except KeyboardInterrupt:
        test_select_keyboardinterrupt()
    else:
        a.append(1)
        select.select([], [F()], [], 0.1)
        test_select_keyboardinterrupt()
        a.append(2)
        select.select([], [], [F()], 0.1)
        test_select
