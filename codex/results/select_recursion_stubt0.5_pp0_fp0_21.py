import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 0)

def test_select_mutated_del():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_del()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 0)

def test_select_mutated_del_attr():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_del_attr()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 0)

def test_select_mutated_del_attr_ref():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_del_attr_ref()
            return a.pop
