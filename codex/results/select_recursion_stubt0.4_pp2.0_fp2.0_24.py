import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [f]
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        raise Exception("didn't raise ValueError")

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a = [f]
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        raise Exception("didn't raise ValueError")

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a = [f, f]
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        raise Exception("didn't raise ValueError")

def test_select_
