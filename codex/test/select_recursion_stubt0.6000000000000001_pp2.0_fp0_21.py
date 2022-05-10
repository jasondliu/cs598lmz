import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    a.append(1)
    select.select([f], [], [])
    a.append(2)
    select.select([f], [], [])

def test_select_mutated_no_fileno():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_no_fileno()
            return a.pop()
    f = F()
    a.append(1)
    # f.fileno is not called
    select.select([f], [], [])
    a.append(2)
    select.select([f], [], [])

def test_select_mutated_no_fileno_no_exc():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_no_fileno_no_exc()
            return a.pop()
    f = F()
    a.append(1)
    # f.fileno is not called
