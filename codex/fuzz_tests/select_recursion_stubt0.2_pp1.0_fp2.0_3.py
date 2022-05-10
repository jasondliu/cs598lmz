import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], [], [], 0)
    a.append(1)
    select.select([], [], [], 0)
    a.append(2)
    select.select([], [], [], 0)
    a.append(3)
    select.select([], [], [], 0)
    a.append(4)
    select.select([], [], [], 0)
    a.append(5)
    select.select([], [], [], 0)
    a.append(6)
    select.select([], [], [], 0)
    a.append(7)
    select.select([], [], [], 0)
    a.append(8)
    select.select([], [], [], 0)
    a.append(9)
    select.select([], [], [], 0)
    a.append(10)
    select.select([], [], [], 0)
    a.append(11)
    select.select([], [], [], 0)
    a.append
