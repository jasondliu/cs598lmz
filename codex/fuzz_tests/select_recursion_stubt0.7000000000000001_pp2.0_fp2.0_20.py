import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    with Selector() as sel:
        sel.register(F(), select.EPOLLIN)
        sel.select()

def test_select_closed():
    with Selector() as sel:
        with open('/dev/null', 'rb') as f:
            fd = f.fileno()
            sel.register(f, select.EPOLLIN)
        sel.unregister(fd)
        with pytest.raises(OSError):
            sel.select()

def test_select_closed2():
    with Selector() as sel:
        with open('/dev/null', 'rb') as f:
            fd = f.fileno()
            sel.register(f, select.EPOLLIN)
        os.close(fd)
        with pytest.raises(OSError):
            sel.select()

def test_select_and_close():
    with open('/dev/null', 'rb') as f:
        with Selector() as sel:
           
