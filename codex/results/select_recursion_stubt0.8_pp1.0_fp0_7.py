import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f)
    for i in range(2):
        try:
            select.select([f], [f], [])
        except KeyboardInterrupt:
            pass

def test_select_exc():
    a = []

    class F:
        def fileno(self):
            raise ValueError
        def close(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [f], [f])
    except ValueError:
        pass
    assert a == [1]

def test_error_zero():
    import _testcapi
    class ZeroDivisionError(Exception):
        pass
    orig = _testcapi.zerodivisionerror_errno
    _testcapi.zerodivisionerror_errno = ZeroDivisionError
    try:
        _testcapi.raise_zerodivisionerror_errno()
    except ZeroDivisionError as e:
        assert e.errno == 0
    else
