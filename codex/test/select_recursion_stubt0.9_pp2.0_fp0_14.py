import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    select.select([F()], a, a, a)
    
def test_select_changed():
    a = []

    class F:
        def fileno(self):
            return 5

    select.select([F()], a, a, a)
    
def test_select_broken():
    class F:
        def fileno(self):
            raise OSError

    try:
        select.select([F()], [F()], [F()], F())
    except OSError:
        pass

class TestCase(unittest.TestCase):
    def test_intrepr(self):
        class F:
            def __int__(self):
                return 5

        assert select.select([], [F()], [], 5.0) == ([], [5], [], 5.0)

    def test_bigfd(self):
        class F:
            def fileno(self):
                return sys.maxsize

