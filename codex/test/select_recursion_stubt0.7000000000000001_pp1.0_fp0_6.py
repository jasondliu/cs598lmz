import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    f = F()
    f.fileno()

    assert a == []
    select.select([f], [], [], 0.0)
    assert a == [1]
    select.select([f], [], [], 0.0)
    assert a == [1, 1]

class test_select_mutated2(object):
    def fileno(self):
        return 1

def test_select_mutated2():
    a = []

    class F(test_select_mutated2):
        def fileno(self):
            a.append(1)
            return 1

    f = F()
    f.fileno()

    assert a == []
    select.select([f], [], [], 0.0)
    assert a == [1]
    select.select([f], [], [], 0.0)
    assert a == [1, 1]

class test_select_mutated3(object):
    def fileno(self):
        return 1

