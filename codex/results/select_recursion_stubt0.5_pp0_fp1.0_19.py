import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    f = F()
    a.append(f)

    # This will raise an exception
    select.select([], [], [], 1)

def test_select_del():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return 0
    f = F()
    a.append(f)

    # This will raise an exception
    select.select([], [], [], 1)

def test_select_dict():
    a = {}

    class F:
        def fileno(self):
            a[0] = 1
            return 0
    f = F()
    a[f] = 1

    # This will raise an exception
    select.select([], [], [], 1)

def test_select_dict_del():
    a = {}

    class F:
        def fileno(self):
            del a[0]
            return 0
    f = F()
    a[f] = 1

    # This will raise an exception
    select.select([], [
