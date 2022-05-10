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

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(1)
    select.select([f], [], [])
    a.append(2)
    try:
        select.select([f], [], [])
    except select.error as e:
        assert e.args[0] == errno.EINTR
    else:
        raise AssertionError("select should be interrupted")

def test_select_interrupted_and_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_interrupted_and_mutated()
            return a.pop()

    f = F()
    a.append(1)
    select.select([f], [],
