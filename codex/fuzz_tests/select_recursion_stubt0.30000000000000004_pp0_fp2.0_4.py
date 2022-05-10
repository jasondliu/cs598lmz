import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            a.append(1)
            return 'a'

    f = F()
    select.select([f], [], [], 1)
    assert a == [1]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

        def read(self):
            a.append(1)
            return 'a'

    f = F()
    select.select([f], [], [], 1)
    assert a == [1]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

        def read(self):
            a.append(1)
            return 'a'

    f = F()
    select.select([f], [], [], 1)
    assert a == [1]

def test_select_mutated_4():
   
