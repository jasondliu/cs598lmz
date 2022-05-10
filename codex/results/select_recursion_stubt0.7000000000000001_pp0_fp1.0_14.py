import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # <- this should not cause an error
            return 0

    f = F()
    fd = f.fileno()

    select.select([fd], [], [], 10) # <- this should not cause an error
