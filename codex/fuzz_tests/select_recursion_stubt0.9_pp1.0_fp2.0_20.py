import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(0)
            return 10
    
    f = F()
    select.select([f],[],[])
