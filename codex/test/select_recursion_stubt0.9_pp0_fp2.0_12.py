import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())

    while True:
        select.select([], [], a)

def test_main():
    test_select_mutated()

