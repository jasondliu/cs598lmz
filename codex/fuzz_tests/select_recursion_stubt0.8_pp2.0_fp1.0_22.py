import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # mutate the list
            a.append('fileno')
            return 42

    f = F()
    select.select([f], [], [])
    assert a == ['fileno']

@pytest.mark.skipif(sys.platform == 'win32',
                    reason="Windows returns syscall error and not EBADF")
def test_select_no_fileno():
    try:
        select.select([object()], [], [])
    except select.error as e:
        assert e.errno == errno.EBADF
    else:
        assert False, "select() didn't raise an error"


def test_select_keyboardinterrupt():
    class StarvingFile(object):
        def fileno(self):
            return 42

    with pytest.raises(select.error) as excinfo:
        select.select([StarvingFile()], [], [])
    assert excinfo.value.args[0] == "select(42, ...): starving"

    # Issue #10881: select(timeout=...) should return immediately

