fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute of a function is a code object
def fn(): pass
assert isinstance(fn.__code__, types.CodeType)

# Test that the __code__ attribute of a function is writable
def fn(): pass
fn.__code__ = fn.__code__

# Test that the __code__ attribute of a function is writable by a code object
def fn(): pass
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# Test that the __code__ attribute of a function is writable by a code object
# with a bad co_argcount
def fn(): pass
try:
    fn.__code__ = types.CodeType(1, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
except ValueError:
    pass
else:
    raise Exception

# Test that the __code__ attribute of a function is writable by a code object
# with a bad co_kwonlyargcount
