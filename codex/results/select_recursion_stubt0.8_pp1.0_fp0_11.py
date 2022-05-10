import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(0)
            return 100

    select.select([F()], [], [], 1)
    assert len(a) == 1
    select.select([F()], [], [], 1)
    assert len(a) == 2


def test_select_exception():
    raised = []

    class F:
        def fileno(self):
            raised.append(0)
            raise ValueError
    select.select([F()], [], [], 1)
    assert len(raised) == 1
    select.select([F()], [], [], 1)
    assert len(raised) == 2


def test_select_renamed():
    import select as s
    s.epoll('hello')


def test_select_abstract():
    class F:
        def fileno(self):
            return 123
    f = F()
    assert select.select([f], [], [], 1.2) == ([f], [], [])
    assert f.fileno() == 123


def test_select_with_dict():
   
