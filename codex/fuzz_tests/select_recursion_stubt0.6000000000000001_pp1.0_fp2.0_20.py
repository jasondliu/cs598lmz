import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def test_select_mutated():
        a.append(F())
        select.select([], a, [])

    test_select_mutated()

class R:
    def read(self):
        return 'a'
    def readinto(self):
        return 'a'
    def close(self):
        pass

def test_select_readinto_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_readinto_mutated()
            return 0

    def test_select_readinto_mutated():
        a.append(F())
        select.select([R()], a, [])

    test_select_readinto_mutated()

def test_select_readinto_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_readinto_mutated_2()
            return 0

    def test_select_readinto_mutated_2():
        a.append(F())
        select.
