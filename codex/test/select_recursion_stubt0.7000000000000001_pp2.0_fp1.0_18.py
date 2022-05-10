import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    result = select.select([], a, a, 0)
    assert len(result) == 3
    assert len(result[1]) == 1
    assert len(result[2]) == 1

class TestException:
    def __init__(self):
        self.closed = False

    def fileno(self):
        return 0

    def close(self):
        self.closed = True

class TestException2:
    def __init__(self):
        self.closed = False

    def fileno(self):
        return 0

    def close(self):
        self.closed = True

    def __repr__(self):
        raise SystemError()

class TestException3:
    def __init__(self):
        self.closed = False

    def fileno(self):
        raise SystemError()

    def close(self):
        self.closed = True

class TestException4:
    def __init__(self):
        self.closed = False

