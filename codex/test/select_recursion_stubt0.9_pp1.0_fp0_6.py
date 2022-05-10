import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    a.append(F())
    a.append(F())

    try:
        select.select(a, [], [])
    except ValueError:
        pass

def test_broken_data():
    a = []
    a.append([])
    # We should get a SettableSocketError rather than TypeError on getting
    # socket.fileno of the list object.
    try:
        select.select(a, [], [])
    except select.SettableSocketError:
        pass

def test_select():
    try:
        select.select([1], [1], [1])
    except TypeError:
        pass
    else:
        print("Bug", "select() must fail when using a non-file object")

def test_select_loop():
    import errno
    import time
    a, b, c = 100, 100, 100
