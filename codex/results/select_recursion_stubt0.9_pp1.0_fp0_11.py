import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # crash expected

    select.select([F()], a, a, 1.0)
