import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    a.append(1)
    select.select([F()], [], [])
    a.append(2)
    select.select([F()], [], [])
    a.append(3)
    select.select([F()], [], [])
    a.append(4)
    select.select([F()], [], [])
    a.append(5)
    select.select([F()], [], [])
    a.append(6)
    select.select([F()], [], [])
    a.append(7)
    select.select([F()], [], [])
    a.append(8)
    select.select([F()], [], [])
    a.append(9)
    select.select([F()], [], [])
    a.append(10)
    select.select([F()], [], [])
    a.append(11)
    select.select([F()], [], [])
