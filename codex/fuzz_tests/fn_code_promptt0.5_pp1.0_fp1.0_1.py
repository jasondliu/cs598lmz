fn = lambda: None
# Test fn.__code__
if hasattr(fn, '__code__'):
    fn.__code__ = None
    fn.__code__ = types.CodeType(
        0, 0, 0, 0, b'', b'', b'', b'', b'', b'', b'', b'', 0, b'')
    fn.__code__ = types.CodeType(
        0, 0, 0, 0, b'', b'', b'', b'', b'', b'', b'', b'', 0, b'',
        0, 0, 0, 0, 0, 0)
# Test fn.__closure__
if hasattr(fn, '__closure__'):
    fn.__closure__ = None
    fn.__closure__ = (None,)
    fn.__closure__ = (None, None)
# Test fn.__defaults__
if hasattr(fn, '__defaults__'):
    fn.__defaults__ = None
    fn.__defaults__ = ()
    fn.__defaults__ = (None,)
    fn.__default
