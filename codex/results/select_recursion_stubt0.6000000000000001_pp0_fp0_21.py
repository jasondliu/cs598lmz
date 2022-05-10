import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class G:
        def fileno(self):
            return 1

    a.append(F())
    select.select([], [], [], 0)
    a.append(G())
    select.select([], [], [], 0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    class G:
        def fileno(self):
            return 1

    a.append(F())
    select.select([], [], [], 0)
    a.append(G())
    select.select([], [], [], 0)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    class G:
        def fileno(self):
            return 1

    a.append(F())
    select.select([], [], [], 0)
    a.append
