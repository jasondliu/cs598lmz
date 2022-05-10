fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__closure__ = None
fn.__globals__ = {}
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__module__ = 'module'

def test_function():
    assert fn.__code__ is fn.__code__
    assert fn.__code__ is not gi.gi_code
    assert fn.__code__ == gi.gi_code
    assert fn.__code__ != fn
    assert fn.__code__ != 0
    assert fn.__code__ != 0.0
    assert fn.__code__ != 'code'
    assert fn.__code__ != b'code'
    assert fn.__code__ != bytearray(b'code')
    assert fn.__code__ != memoryview(b'code')
    assert fn.__code__ != Ellipsis
    assert fn.__code__ != Not
