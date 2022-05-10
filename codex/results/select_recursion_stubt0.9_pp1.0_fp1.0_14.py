import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    try:
        select.select([f], [], [])
    except Exception, e:
        print 'select failed:', e

def test_path_not_in_sys_path():
    """Test path not in sys.path."""
    class F:
        def fileno(self):
            return 42

    try:
        select.select([F()], [], [])
        assert False
    except ImportError, e:
        print 'import failed as expected:', e
    except TypeError, e:
        print 'BytesWarning should not be emitted:', e

test_select_mutated()
test_path_not_in_sys_path()
print 'done'
