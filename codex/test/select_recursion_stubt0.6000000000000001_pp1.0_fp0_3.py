import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [], 0)
    select.select(a, [], [], 0)
    select.select([], [], [], 0)
    select.select([], a, [], 0)
    select.select([], [], a, 0)
    select.select([], [], [], 0)
    select.select([], [], [], 0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [], 0)
    select.select(a, [], [], 0)
    select.select([], [], [], 0)
    select.select([], a, [], 0)
    select.select([], [], a, 0)
    select.select([], [], [], 0)
    select.select([], [], [], 0)

def test_select_mutated_3():
    a = []

