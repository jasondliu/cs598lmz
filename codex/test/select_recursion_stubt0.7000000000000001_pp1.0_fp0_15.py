import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([], [F()], [])

# test that select works with custom objects that have a fileno() method
# but raises an error when that object is mutated during the select() call
with self_executing_context():
    test_select_mutated()
