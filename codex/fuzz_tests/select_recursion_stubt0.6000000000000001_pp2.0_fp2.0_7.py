import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

        def close(self):
            pass

    select.select([1,F(),2,3], [], [])
    assert a == [2, 3]

def test_select_mutated_2():
    a = [1,2,3]
    class F:
        def fileno(self):
            test_select_mutated_2()
            return a.pop()
        def close(self):
            pass

    select.select([F(),2,3,F()], [], [])
    assert a == [3]

def test_select_mutated_3():
    a = [1,2,3]
    class F:
        def fileno(self):
            test_select_mutated_3()
            return a.pop()
        def close(self):
            pass
    select.select([1,F(),2,3,F()], [], [])
    assert a == [3]
