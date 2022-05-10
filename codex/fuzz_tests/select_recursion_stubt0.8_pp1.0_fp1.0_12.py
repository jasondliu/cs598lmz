import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # <-- this mutates the list
            return 0
    a.append(F())
    try:
        select.select(a,a,a,0.0)
    except ValueError:
        pass
    else:
        raise AssertionError

def test_select_interrupted():
    a = []
    class F:
        def fileno(self):
            return 0
    a.append(F())
    try:
        os.read(0, 1)
    except OSError as e:
        if e.errno != errno.EAGAIN:
            raise
    else:
        raise AssertionError
    try:
        select.select(a,a,a,0.0)
    except select.error as e:
        if e.args[0] != errno.EINTR:
            raise
    else:
        raise AssertionError
    try:
        os.read(0, 1)
    except OSError as e:
        if e.errno != errno.EAGAIN:
            raise

