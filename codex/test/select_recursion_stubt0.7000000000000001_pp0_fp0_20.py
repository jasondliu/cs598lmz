import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return f.fileno()
        def close(self):
            pass

    f = F()
    a.append(f)
    for i in range(4):
        try:
            select.select(a, a, a, 2)
        except select.error:
            pass
    a.remove(f)
    f.close()

def test_select_list_mutated():
    a = []
    b = []
    c = []

    class F:
        def fileno(self):
            test_select_list_mutated()
            return f.fileno()
        def close(self):
            pass

    f = F()
    a.append(f)
    for i in range(4):
        try:
            select.select(a, b, c, 2)
        except select.error:
            pass
    a.remove(f)
    f.close()

def test_select_invalid():
    class F:
        def fileno(self):
            return f.fileno()
