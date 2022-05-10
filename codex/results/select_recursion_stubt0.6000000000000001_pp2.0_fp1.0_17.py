import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_interrupted():
    def r(f):
        try:
            select.select([f], [], [], 0)
        except select.error:
            pass
    
    a = []
    
    class F:
        def fileno(self):
            a.append(1)
            r(self)
            return a.pop()
    
    r(F())
