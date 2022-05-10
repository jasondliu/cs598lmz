import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    a.append(1)
    select.select([], [], [])
    a.append(2)
    select.select([], [], [])
    a.append(3)
    select.select([], [], [])
    a.append(4)
    select.select([], [], [])
    a.append(5)
    select.select([], [], [])
    a.append(6)
    select.select([], [], [])
    a.append(7)
    select.select([], [], [])
    a.append(8)
    select.select([], [], [])
    a.append(9)
    select.select([], [], [])
    a.append(10)
    select.select([], [], [])
    a.append(11)
    select.select([], [], [])
    a.append(12)
    select.select([], [], [])
    a.append(13)
   
