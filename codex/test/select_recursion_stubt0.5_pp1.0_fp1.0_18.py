import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    try:
        select.select([F()], [F()], [F()])
    except IndexError:
        return
    except:
        pass
    raise Exception("didn't raise IndexError")

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    try:
        select.select([F()], [F()], [F()], 0)
    except IndexError:
        return
    except:
        pass
    raise Exception("didn't raise IndexError")

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            return a.pop()

