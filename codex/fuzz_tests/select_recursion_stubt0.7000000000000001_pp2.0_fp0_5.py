import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 3

    select.select([F()], [], [], 0)
    if a != None:
        raise Exception("F.fileno() was not called")

def test_select_error():
    a = []
    class F:
        def fileno(self):
            try:
                raise ZeroDivisionError
            except:
                a.append(1)
                return 3
    select.select([F()], [], [], 0)
    if a == []:
        raise Exception("ZeroDivisionError was not thrown")
