fn = lambda: None
# Test fn.__code__.co_freevars
fn.__code__ = types.FunctionType(
    types.CodeType(
        0,
        0,
        0,
        0,
        b'',
        b'',
        b'',
        0,
        b'',
        (),
        (),
        (),
        b'',
        b'',
        0,
        b'',
        (),
    ),
    {},
    'fn',
    (),
    (),
).__code__

try:
    fn.__code__.co_freevars = ()
except TypeError:
    print('co_freevars must be a tuple of strings')
else:
    raise test.TestFailed('expected TypeError from setting co_freevars')

# Test fn.__closure__
fn.__closure__ = ()
try:
    del fn.__closure__
except TypeError:
    pass
else:
    raise test.TestFailed('expected TypeError from deleting __closure__')
try:
    fn.__closure__ = (1, 2)
