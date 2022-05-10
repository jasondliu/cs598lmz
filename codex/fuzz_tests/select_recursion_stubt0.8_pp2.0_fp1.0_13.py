import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 8

    a.append(F())
    select.select([], [], [], 0)

def test_absolute_import():
    import __future__
    prev_absolute_import = __future__.absolute_import
    try:
        __future__.absolute_import = True
        # This is a relative import, it must not work now
        import sys
    except ImportError:
        print('Passed test_absolute_import')
    else:
        raise AssertionError('Relative import in absolute_import mode')
    finally:
        __future__.absolute_import = prev_absolute_import

def test_absolute_import_invalid_future():
    import __future__
    prev_absolute_import = __future__.absolute_import
    try:
        __future__.absolute_import = -1
    except ValueError:
        print('Passed test_absolute_import_invalid_future')
    else:
        raise AssertionError('Invalid future value for absolute_import was not caught ')
    finally:
        __future__.absolute
