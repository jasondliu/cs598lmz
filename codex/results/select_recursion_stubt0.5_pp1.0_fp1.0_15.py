import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except RuntimeError:
        pass
    else:
        print("expected RuntimeError")

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return 1
    f = F()
    a.append(f)
    select.select([f], [], [])
    a.pop()
    try:
        select.select([f], [], [])
    except RuntimeError:
        pass
    else:
        print("expected RuntimeError")

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return 1
    f = F()
    a.append(f)
    select.select([f], [], [])
    a[0] = None
    try:
        select.select([f], [], [])
    except RuntimeError:
        pass
    else:
       
