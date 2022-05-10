import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3
    a.append(F())

    mutate_event()
    time.sleep(0.1)
    select.select(a, [], [], 1)
