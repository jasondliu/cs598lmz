import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4
        def close(self):
            a.append("closed")

    tgt = []
    try:
        select.select([F()], [], [], 0)
    except RuntimeError:
        tgt.append("exception")
    assert tgt == ["exception"]
    assert a == []

def test_select_missing_close():
    import gc
    leaks = []

    class F:
        def __init__(self):
            self.closed = False
        def __del__(self):
            if not self.closed:
                leaks.append("leaked")
        def fileno(self):
            return 4
        def close(self):
            self.closed = True

    select.select([F()], [], [], 0)
    del f
    gc.collect()
    assert leaks == []
