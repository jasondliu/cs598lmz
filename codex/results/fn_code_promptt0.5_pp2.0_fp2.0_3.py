fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = _code(['x', 'y'], [], [], [], [], [], [], '', '', 0, b'')
assert fn.__code__.co_varnames == ('x', 'y')

# Test fn.__code__.co_argcount
fn.__code__ = _code([], [], [], [], [], [], [], '', '', 0, b'')
assert fn.__code__.co_argcount == 0
fn.__code__ = _code(['x'], [], [], [], [], [], [], '', '', 0, b'')
assert fn.__code__.co_argcount == 1
fn.__code__ = _code(['x', 'y'], [], [], [], [], [], [], '', '', 0, b'')
assert fn.__code__.co_argcount == 2

# Test fn.__code__.co_cellvars
fn.__code__ = _code([], [], [],
