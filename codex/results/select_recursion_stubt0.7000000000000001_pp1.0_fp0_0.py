import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def readline(self):
            a.append(1)
            return 'a'

    f = F()
    fd = f.fileno()
    assert select.select([fd], [], []) == ([fd], [], [])
    assert select.select([fd], [], []) == ([fd], [], [])
    assert a == [1, 1]

if __name__ == '__main__':
    test_select_mutated()
