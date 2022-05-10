import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            assert a == [], "mutating during iteration... no bueno."
            a.append(True)
            1/0
    F()
    assert select.select([F()], [], [], 1.0) == ([], [], [])
    assert a == [True], a

def test_select_duplicate_fds():
    a = []
    class F:
        def fileno(self):
            a.append(True)
            return 1
    assert select.select([F(), F(), F()], [], [], 1.0) == ([], [], [])
    assert a == [True, True, True]
