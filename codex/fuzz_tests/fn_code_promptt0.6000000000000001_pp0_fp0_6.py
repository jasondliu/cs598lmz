fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 0, b'')
fn()

# Test fn.__code__.co_cellvars
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 0, b'', ())
fn()

# Test fn.__code__.co_names
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 0, b'', (), ())
fn()

# Test fn.__code__.co_consts
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 0, b'', (), (), ())
fn()

# Test fn.__code__.co_filename
fn.__code__ = types
