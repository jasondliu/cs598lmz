import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        return 1

    select.select([F()], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
    select.select([], [], [], 0.0)
