import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    class C:
        def close(self):
            pass
    
    class B:
        def close(self):
            a.append(2)

    select.select([F(), C()], [F(), C()], [F(), C(), B()])
    assert len(a) == 4
    assert a[0] == 1
    assert a[1] == 2
    assert a[2] == 2
    assert a[3] == 1
