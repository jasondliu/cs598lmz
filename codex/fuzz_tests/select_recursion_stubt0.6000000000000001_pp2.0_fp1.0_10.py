import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            a.append(1)
            return 'test'
    class F2:
        def fileno(self):
            return 0
        def read(self):
            return 'test'
    f = F()
    f2 = F2()
    for i in range(10):
        select.select([f], [], [], 0)
    assert a == [1] * 10
    select.select([f2], [], [], 0)
    assert a == [1] * 10
