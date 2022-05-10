import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise BlockingIOError
    select.select([F()], a, a, 0)
    1/0

def test_select_mutated_with():
    def 
