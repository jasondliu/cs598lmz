import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(2)

    old_size = sys.getrecursionlimit()
    import _testcapi
    _testcapi.set_recursion_limit(100)
    try:
        select.select([F()], [], [], None)
    except RecursionError:
        pass
    assert a == [], "a = %s" % a
    _testcapi.set_recursion_limit(old_size)

def test_select_large_fd():
    ok = False
    try:
        select.select([], [], [80000], None)
    except ValueError:
        ok = True
    assert ok

def test_sys_getfilesystemencoding():
    assert type(sys.getfilesystemencoding()) == str

@pytest.mark.skipif("os.name != 'posix' or 'apple' in sys.platform")
def test_sys_getdefaultencoding():
    assert sys.getdefaultencoding() == 'utf-8'
