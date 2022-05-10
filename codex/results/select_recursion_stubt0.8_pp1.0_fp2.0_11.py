import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 3
    
    class B:
        def fileno(self):
            test_select_mutated()
            a.append(2)
            return 5
    
    l = select.select([F()], [B()], [], 1)
    print(l)

    assert a != [], "select didn't call fileno()"
    a.sort()
    assert a == [1, 2], "select didn't call fileno()"

run_test(__name__)
