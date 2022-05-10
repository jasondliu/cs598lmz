import select
# Test select.select()

def test_select():
    # Test basic operation
    r, w, x = select.select([], [], [], 0)
    assert len(r) == len(w) == len(x) == 0
    # Test that it checks for bad file descriptors.
    try:
        select.select([object()], [], [])
    except TypeError:
        pass
    else:
        assert False, "expected exception"
    # Test exception handling
    class BadFileDescriptor:
        def fileno(self):
            return 'fileno'
    try:
        select.select([BadFileDescriptor()], [], [])
    except TypeError:
        pass
    else:
        assert False, "expected exception"
    # Test that it checks for bad timeouts
    try:
        select.select([], [], [], object())
    except TypeError:
        pass
    else:
        assert False, "expected exception"

def test_poll():
    # Test basic operation
    p = select.poll()
