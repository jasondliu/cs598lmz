import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    F.__module__ = 'builtins'

    def main():
        f = F()
        a.append(f.fileno())
        select.select([f], [f], [f])

    main()

def test_select_mutated_exception():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_exception()
            return a[0]

    F.__module__ = 'builtins'

    def main():
        f = F()
        a.append(f.fileno())
        try:
            select.select([f], [f], [f])
        except IndexError:
            pass

    main()

def test_select_mutated_exception_nested():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_exception_nested()
            return a[0]

    F.__module__ = 'builtins'

    def main():
        f = F()
       
