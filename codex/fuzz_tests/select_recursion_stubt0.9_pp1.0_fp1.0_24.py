import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # => RuntimeError: maximum recursion depth exceeded
            a.append(1)
            return 0

    select.select([F()], [F()], [F()])
