import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def read(self):
            a.append(1)
            return "1"

    f = F()
    select.select([f], [], [], 0.1)
    assert a == [1]

def test_select_mutated_with_timeout():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_with_timeout()
            return 1

        def read(self):
            a.append(1)
            return "1"

    f = F()
    select.select([f], [], [], 0.1)
    assert a == [1]

def test_select_mutated_with_timeout_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_with_timeout_2()
            return 1

        def read(self):
            a.append(1)
            return "1"

    f = F()
    select.select([f], [], [], 0.1)
    assert a
