import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def callback():
        select.select([F()], a, a)
        callback()

    callback()
