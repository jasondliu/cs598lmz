import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(F)

        
    isinstance(select.select([F()], [], []), (list, tuple))


def test_select_with_bad_fd():
    s = socket.socket()
    s.close()
    try:
        select.select([s], [], [])
    except ValueError as err:
        assert isinstance(err, ValueError), '%r should be ValueError' % (type(err),)
        assert str(err) == 'Filedescriptor out of range in select()'
    else:
        raise Exception('Did not raise ValueError')


def test_select_large_fd():
    ok = True
    try:
        select.select({10000000}, {10000000}, {10000000})
    except ValueError:
        ok = False
    assert ok


@pytest.mark.skipif('True')
def test_select():
    readable = []
    writable = []
    errorable = []
    try:
        r, w, e = select.select(readable, writable, errorable
