import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[-1]
            #raise IndexError

        def recv(self, b):
            a.pop()
            return b""

    sel = selectors.BaseSelector()
    sel.register(F(), selectors.EVENT_READ)
    sel.register(F(), selectors.EVENT_READ)
    sel.register(F(), selectors.EVENT_READ)
    sel.register(F(), selectors.EVENT_READ)

    a = list(range(len(sel.selectors)))
    random.shuffle(a)

    try:
        sel.select()
    except IndexError:
        pass
    else:
        assert False, "IndexError not thrown"

def make_socket():
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.bind(("127.0.0.1", 0))
    so.setblocking(False)
    return so

def select_exhaust():
    sel = selectors.BaseSelector()

