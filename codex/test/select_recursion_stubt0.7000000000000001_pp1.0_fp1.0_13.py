import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # <-- this calls 'select', which may mutate 'a'
            return len(a)

    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])
    del a[:]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2() # <-- this calls 'select', which may mutate 'a'
            return len(a)

    select.select([F()], [], [])
    del a[:]
    select.select([F()], [], [])
