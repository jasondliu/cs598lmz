import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()

    def callback(*args):
        a.append(1)

    select.select([f], [], [], 0)
    select.select([], [f], [], 0)
    select.select([], [], [f], 0)

    select.select([f], [], [], 0, callback)
    select.select([], [f], [], 0, callback)
    select.select([], [], [f], 0, callback)
