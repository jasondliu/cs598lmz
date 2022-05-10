fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test'
fn.__qualname__ = 'test'
fn.__module__ = 'test'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__closure__ = fn.__globals__ = ()
fn.__dict__ = {}
fn.__doc__ = None
fn.__text_signature__ = None

# test that __text_signature__ is not set for built-in functions
# (see issue #12962)
for name in dir(__builtins__):
    if name.startswith('__'):
        continue

    # __import__ is a special case
    if name == '__import__':
        continue

    f = getattr(__builtins__, name)
    assert f.__text_signature__ is None

# test that __text_signature__ is set for functions defined in C
def test_text_signature_for_c_functions():
    import _testcapi

