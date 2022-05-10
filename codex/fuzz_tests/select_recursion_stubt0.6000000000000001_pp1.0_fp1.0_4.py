import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    s = select.select([], [], [F(), F()], 0)
    assert s == ([], [], [])

def test_select_keyboard_interrupt():
    a = []

    class F:
        def fileno(self):
            test_select_keyboard_interrupt()
            return a.pop()

    def raise_keyboard_interrupt():
        raise KeyboardInterrupt

    s = select.select([], [], [F(), F()], 0)
    assert s == ([], [], [])

class TestSelect:
    def setup_class(cls):
        cls.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.serv.bind(('localhost', 0))
        cls.serv.listen(5)
        cls.port = cls.serv.getsockname()[1]
        cls.cli1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.cli1
