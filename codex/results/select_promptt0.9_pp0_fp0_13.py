import select
# Test select.select() and select.error().
try:
    import _testcapi
except ImportError:
    pass
else:
    err = _testcapi.get_errno()
    _testcapi.set_errno(42)
    try:
        rd, wd, xd = select.select([], [], [], -1)
    except select.error:
        pass

    # Only check that a select.error was raised, not on the exact error
    # code.  Different platforms raise different codes.
    if _testcapi.get_errno() == err:
        raise Exception("select.error not called")

    _testcapi.set_errno(0)
