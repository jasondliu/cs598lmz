import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    a.append(f)
    try:
        select.select(a, a, a)
   
