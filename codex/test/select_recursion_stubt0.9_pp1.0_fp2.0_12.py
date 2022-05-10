import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

        def close(self):
            a.append(1)

    f = F()
    with pytest.raises(RecursionError):
        select.select([f], [], [], 1.0)

    f.close()
    assert a == [1]

@pytest.mark.skipif(not hasattr(select, 'devpoll'),
                    reason='select has been replaced with ffi rffi')
@pytest.mark.skipif(not test_support.is_linux,
                    reason='''
                    rlinux.c doesn't emulate the old devpoll, see rffi.py
                    line 230.
                    ''')
def test_devpoll():
    a = []

    class F:
        def fileno(self):
            test_support.SAMPLE_FILENO

        def close(self):
            a.append(1)

    f = F()
    dp = select.devpoll()

