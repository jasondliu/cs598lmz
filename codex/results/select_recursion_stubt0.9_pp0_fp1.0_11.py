import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 99

    def add():
        a.append(F())
        a.append(1)

    def remove(i):
        del a[i]

    add()

    old_len = len(a)
    for i in range(len(a)):
        remove(i)
        add()

def test_select_bad_read_list():
    import socket
    s = socket.socket()
    s.bind(('localhost', 0))
    s.listen(1)
    s.accept()
    return select.select([s], [], [])

def test_select_interrupted_error():
    import select
    import socket
    import errno
    class badfd:
        def fileno(self):
            return -42
    try:
        select.select([badfd()], [], [])
    except OSError as e:
        assert e.errno == errno.EBADF
    else:
        pytest.fail('Expected OSError')

def test_select_unicode_error():

