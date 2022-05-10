import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
        def __getitem__(self, index):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

class C:
    def __getitem__(self, i):
        return i

def test_select_bad():
    raises(TypeError, select.select, 1, 2, 3)
    raises(TypeError, select.select, [1], 2, 3)
    raises(TypeError, select.select, [1], [2], 3)
    raises(TypeError, select.select, [1], [2], [3])
    raises(TypeError, select.select, [C()], [C()], [C()])
    raises(TypeError, select.select, [1], [2], [3], 4)

