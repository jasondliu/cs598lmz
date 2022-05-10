import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    obj = F()
    select.select([obj], [], [])

    assert a == [1]

def test_select_error():
    import select, sys
    try:
        select.select([1], [], [])
    except select.error as e:
        assert e.args == (9, "Bad file descriptor")
    except Exception:
        err = sys.exc_info()[1]
        assert 'Bad file descriptor' in err.args[0]
    else:
        pytest.fail("exception not raised")
