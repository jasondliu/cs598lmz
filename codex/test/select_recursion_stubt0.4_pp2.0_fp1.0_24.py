import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_mutated_again():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_again()
            return len(a)
        def close(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_mutated_again_again():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_again_again()
            return len(a)
        def close(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_mutated_again_again_again():
    a = []

    class F:
        def fileno(self):
            test_select_
