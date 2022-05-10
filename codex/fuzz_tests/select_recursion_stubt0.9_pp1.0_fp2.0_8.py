import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    select.select([], a, [])

def test_select_closed():
    a = []
    b = []
    a.append(test_select_closed)
    b.append(test_select_closed)
    try:
        select.select([], a, b)
    except:
        pass
    a.append(test_select_closed)
    b.append(test_select_closed)
    try:
        select.select([], a, b)
    except:
        pass
