import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

        def read(self):
            a.append(1)
            return 'a'

    f = F()
    s = select.select([f], [], [])
    assert a == [1]
    assert s == ([f], [], [])

def test_select_mutated2():
    import os, sys
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 5

        def read(self):
            a.append(1)
            return 'a'

    f = F()
    s = select.select([f], [], [], 0.0)
    assert a == [1]
    assert s == ([], [], [])

def test_select_mutated3():
    import os, sys
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 5

        def read(self):
            a.append(1)
            return 'a'

        def write(self,
