import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def close(self):
            a.append(1)
    f = F()
    try:
        select.select([f], [], [])
    except ValueError as ex:
        assert str(ex) == "I/O operation on closed file."
        assert a, "close method not called"
    else:
        assert False, "ValueError not raised"
    assert a, "close method not called"
    assert f.closed, "close attribute not set"

if __name__ == "__main__":
    test_select_mutated()
