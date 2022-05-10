import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def f(*args, **kwargs):
        try:
            a.append(1)
            a.append(2)
            test_select_mutated()
            a.append(3)
            a.append(4)
        except IndexError:
            a.append(5)
            a.append(6)
        except:
            a.append(7)
            a.append(8)
        else:
            a.append(9)
            a.append(10)
        return a



    b = f(select.select, [F()], [], [], 30.0)
    assert b is a
    assert a == [1, 2, 9, 10]

def test_select_mutated2():
    a = []
    class F:
        def fileno(self):
            raise IndexError
            return 1

