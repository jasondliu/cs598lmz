import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # mutate a
            return 1
    f = F()

    a.append(f)
    select.select([], [], a, 0.0)
    a.pop()
    select.select([], [], a, 0.0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 1
        def close(self):
            a.append(1)
    f = F()

    a.append(f)
    select.select([], [], a, 0.0)
    a.pop()
    select.select([], [], a, 0.0)

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 1
        def close(self):
            a.append(1)
            test_select_closed_mutated() # mutate a
    f = F()

    a.append(f)
    select.select([], [], a, 0.0)
    a.pop()
   
