import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # <-- this is a mutation
            return 42

    class G:
        def fileno(self):
            return 42

    assert  select.select([], a, a, 0)
    del a[:]
    assert select.select([F()], a, a, 0)
    del a[:]
    assert not select.select([G()], a, a, 0)
    del a[:]
    assert select.select([], a, a, 0)
