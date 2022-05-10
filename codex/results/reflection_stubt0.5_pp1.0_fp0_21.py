fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), '', b'', 0, b'')
fn.__code__.co_lnotab = b'A'
print(fn.__code__.co_lnotab)
fn.__code__.co_lnotab = b'\x01'
print(fn.__code__.co_lnotab)

# Issue #20483: test that we can assign to co_lnotab.
def f(): pass
f.__code__.co_lnotab = b'\x01'
print(f.__code__.co_lnotab)

# Issue #20485: test that we can assign to co_firstlineno.
def f(): pass
f.__code__.co_firstlineno = 2
print(f.__code__.co_firstlineno)

# Issue #20486: test that we can assign to co_name.
def f(): pass
f.__code__.co_name = '
