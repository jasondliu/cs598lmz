import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self, bytes):
            a.append(bytes)
            return b'x'

    select.select([F()], [], [])
    assert a == [1]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0

        def read(self, bytes):
            a.append(bytes)
            return b'x'

    select.select([F()], [], [], 1.0)
    assert a == [1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 0

        def read(self, bytes):
            a.append(bytes)
            return b'x'

    select.select([F()], [], [], 1.0, 1.0)
    assert a == [1]

def test_select_mutated4():
    a = []

   
