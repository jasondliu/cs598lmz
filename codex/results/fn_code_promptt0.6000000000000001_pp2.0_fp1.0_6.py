fn = lambda: None
# Test fn.__code__
fn.__code__ = 'test_code'
fn.__code__ = Code(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
# Test fn.__closure__
fn.__closure__ = 'test_closure'
fn.__closure__ = (Cell(0),)
# Test fn.__defaults__
fn.__defaults__ = 'test_defaults'
fn.__defaults__ = (0,)
# Test fn.__globals__
fn.__globals__ = 'test_globals'
fn.__globals__ = {}
# Test fn.__kwdefaults__
fn.__kwdefaults__ = 'test_kwdefaults'
fn.__kwdefaults__ = {'a': 0}
# Test fn.__name__
fn.__name__ = 'test_name'
fn.__name__ = 'a'
# Test fn.__qualname__
fn.__qualname__ = 'test_qualname'
fn.__qualname__ = 'a'

#
