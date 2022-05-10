import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return None

    class G:
        def fileno(self):
            a.append(G())
            return None

    a = [F(), G()]
    try:
        select.select(a, a, a)
    except select.error as e:
        assert e.args[0] == errno.EBADF
    else:
        assert False

    class H:
        def fileno(self):
            a.append(H())
            return None

    a = [F(), H()]
    try:
        select.select(a, a, a)
    except select.error as e:
        assert e.args[0] == errno.EBADF
    else:
        assert False

def test_select_error(monkeypatch):
    a = []

    class F:
        def fileno(self):
            raise ZeroDivisionError
            return None

    class G:
        def fileno(self):
            a.append(G())
            return None

    a = [F(), G()]
    try:
        select
