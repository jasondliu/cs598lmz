import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    def set_non_blocking(fd):
        pass

    def close(fd):
        a.append('close')

    select.select = lambda r, w, e, t: [[F()], [], []]
    select.set_non_blocking = set_non_blocking
    select.close = close
    select.poll()

    assert a == ['close']
