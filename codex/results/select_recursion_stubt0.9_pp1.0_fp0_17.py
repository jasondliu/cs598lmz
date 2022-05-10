import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4

    a.append(F())

    p = select.poll()
    p.register(a[0])
    p.register(5)
    p.poll()

def test_select_keyerror():
    p = select.poll()
    try:
        p.unregister(4)
    except KeyError:
        pass
    else:
        raise RuntimeError

def test_select_error():
    p = select.poll()
    try:
        p.register(1, 'spam')
    except ValueError:
        pass
    else:
        raise RuntimeError
