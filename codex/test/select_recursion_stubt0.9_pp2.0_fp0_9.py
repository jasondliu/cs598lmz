import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # this used to crash
            return -1

    select.select([F()], a, a, 10)

#~ print test_select_mutated()
