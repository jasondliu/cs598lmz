import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def read(self): pass
        
    f = F()

    try:
        select.select([f], a, a)
    except RuntimeError:
        pass
