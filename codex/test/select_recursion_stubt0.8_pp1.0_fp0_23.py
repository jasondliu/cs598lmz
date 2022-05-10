import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1


    a.append(F())
    try:
        select.select([], a, a, 1)
    except:
        pass
    a[0].fileno()

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 1


    a.append(F())
    try:
        select.select([], a, a, 1)
    except:
        pass
    select.select([], a, a, 1)

def test_select_mutated_3():
    a = []
    class F:
        def fileno(self):
            return 1
    a.append(F())

    class F2:
        def fileno(self):
            test_select_mutated_3()
            return 1
    try:
        select.select([], a, a, 1)
    except:
        pass
    a.append(F2())
    select.select([], a, a, 1)

