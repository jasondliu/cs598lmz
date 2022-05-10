fn = lambda: None
# Test fn.__code__ if possible. Otherwise, test fn.code_object
fn.__code__ = sys._getframe().f_code
fn_code = getattr(fn, '__code__', None) or getattr(fn, 'func_code', None)
if fn_code is None: # pragma: no cover
    # Cannot properly detect Python version.
    sys.exit('WARNING: Cannot detect Python version.')
# Patching needed for Python3!
if PY3 and fn_code:
    fn_code.co_flags &= ~CO_NESTED
