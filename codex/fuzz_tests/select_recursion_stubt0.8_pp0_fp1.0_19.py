import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    f = F()
    a.append(f)

    select.select(a, a, a)

def test_select_fileno():
    class F:
        pass
    f = F()

    try:
        select.select([f], [f], [f])
    except AttributeError:
        pass
    else:
        fail("expected AttributeError")

def test_select_list():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1
    f = F()
    select.select([f], [f], [f])
    select.select([f], [f], [f])

def test_select_timeout():
    select.select([], [], [], 0.2)
