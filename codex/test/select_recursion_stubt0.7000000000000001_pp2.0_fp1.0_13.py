import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 10

    a.append(F())
    a.append(F())
    a.append(F())
    a.append(F())
    a.append(F())

    test_select_mutated.counter += 1
    if test_select_mutated.counter > 100:
        return

    try:
        select.select(a,a,[])
    except ValueError:
        pass


test_select_mutated.counter = 0

def test_select_exc():
    import _socket

    sock = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    try:
        select.select([sock], [sock], [sock])
    except:
        pass
    test_select_exc.counter += 1
    if test_select_exc.counter > 100:
        return
    test_select_exc()

test_select_exc.counter = 0

def test_select_timeout(timeout=0.5, count=1000):
    import _socket
