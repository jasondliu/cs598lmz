import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            print('fileno')
            return 123

        def read(self, n):
            return bytes(a)

    f = F()
    del a[:]
    select.select([f], [], [])

def test_select_mutated_nested():
    a = []

    class F:
        def fileno(self):
            f = F()
            del a[:]
            select.select([f], [], [])
            print('fileno')
            return 123

        def read(self, n):
            return bytes(a)

    f = F()
    del a[:]
    select.select([f], [], [])

def test_select_mutated_nested_twice():
    a = []

    class F:
        def fileno(self):
            f = F()
            del a[:]
            select.select([f], [], [])
            print('fileno')
            return 123

        def read(self, n):
            return bytes(a)

    f = F()
    del a[:]

