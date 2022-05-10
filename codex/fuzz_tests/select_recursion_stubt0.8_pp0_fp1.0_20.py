import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # mutate 'a' during select
            return a.pop()

    a = [F(), F()]
    select.select([], [], [])
</code>

