import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    try:
        select.select([], [], [], 1)
    except ValueError:
        pass


def test_select_broken_connection():
    a, b = socket.socketpair()
    try:
        a.send(b"123")
        a.close()
        select.select([b], [], [], 1)
    except OSError:
        pass
    finally:
        a.close()
        b.close()

def test_select_with_file():
    f = open(__file__, 'rb')
    try:
        select.select([f], [], [], 1)
    except ValueError:
        pass
    finally:
        f.close()
