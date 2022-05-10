import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # infinite recursion
            return a.pop()

    class X:
        def __init__(self):
            self.f = F()

    x = X()
    a = [x.f]
    try:
        select.select([x.f], [], [], None)
    except RuntimeError:
        pass
