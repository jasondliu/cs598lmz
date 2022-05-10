fn = lambda: None
# Test fn.__code__.co_argcount.
try:
    fn()
except TypeError as e:
    if not str(e).startswith('fn() takes no arguments'):
        raise SystemExit('Unexpected exception message: ' + str(e))
else:
    raise SystemExit('expected TypeError')


# Test fn.__code__.co_filename.
if fn.__code__.co_filename != '<example.py>':
    raise SystemExit('Wrong co_filename: ' + fn.__code__.co_filename)


# Test fn.__code__.co_firstlineno.
if fn.__code__.co_firstlineno != example.__line__:
    raise SystemExit(
        'Wrong co_firstlineno: ' + repr(fn.__code__.co_firstlineno))


# Test fn.__code__.co_lnotab.
# This is just a sanity check to test whether the data is available.
if not fn.__code__.co_lnotab:
    raise SystemExit('co_lnotab is empty
