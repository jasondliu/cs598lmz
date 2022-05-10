import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [], 0)

    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.append(6)
    a.append(7)
    a.append(8)
    a.append(9)
    a.append(10)
    a.append(11)
    a.append(12)
    a.append(13)
    a.append(14)
    a.append(15)
    a.append(16)
    a.append(17)
    a.append(18)
    a.append(19)
    a.append(20)
    a.append(21)
    a.append(22)
    a.append(23)
    a.append(24)
    a.append(25)
    a.append(26)
    a.append(27)
    a.append(28)
    a.append(29)
    a.
