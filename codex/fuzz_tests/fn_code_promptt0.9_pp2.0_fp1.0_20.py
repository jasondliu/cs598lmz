fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), '', b'', b'', 0, b''
)
fn.__code__.co_varnames = ()
# Test arg.__doc__
fn.__code__.co_varnames = (
    'A', 'B', 'C', 'D', 'E', 'self', 'Model', 'f', 'field_name'
)
fn.__defaults__ = ()
# Test that *a becomes *args
fn.__defaults__ = (1,)
# Test that *a, **k becomes *args, **kwargs
fn.__defaults__ = (1, 2)
# Test that *a, b becomes *a, b
fn.__defaults__ = (1, 2, 3)
# Test that fn.__annotations__
fn.__annotations__ = {}
# Test that fn.__annotations__ with a non-trivial case
fn.__defaults__ = (1, 2
