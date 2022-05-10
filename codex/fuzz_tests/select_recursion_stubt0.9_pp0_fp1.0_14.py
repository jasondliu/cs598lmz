import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    b = [F()]
    try:
        select.select(a,b,a,0)
    except ValueError as e:
        pass

def test_select_replacing():
    a = []
    b = []
    class F:
        def fileno(self):
            return a.pop(0)

    f = F()
    b.append(f)
    b.append(f)
    try:
        select.select([f],b,a,0)
    except ValueError as e:
        pass
    # Now swap the replacement
    a.append(f.fileno())
    a.append(1)
    b[0] = 1
    select.select([f],b,a,0)

def test_select_raised():
    # A fileno() method that raises an exception
    def fileno():
        raise OSError("I do believe we're stuck")

    foo = type("Foo", (object,), dict(fileno=fileno))()
    try:
        select.select([foo], [
