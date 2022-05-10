import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            if len(a) == 0:
                raise KeyError
            else: 
                return a.pop()
        
    a.append(1)
    obj = F()
    def test1():
        return obj
    def test2():
        a.append(2)
        return obj

    select.select([test1()], [], [])
    result = select.select([test2()], [], [])
    assert len(result[0]) == 1
    assert len(result[1]) == 0
    assert len(result[2]) == 0
