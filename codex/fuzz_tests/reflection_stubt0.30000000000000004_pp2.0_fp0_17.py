fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__doc__ = 'bar'
fn.__dict__ = {'baz': 'qux'}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (1, 2, 3)
fn.__globals__ = {'a': 'b'}
fn.__module__ = 'quux'
fn.__annotations__ = {'corge': 'grault'}
fn.__kwdefaults__ = {'garply': 'waldo'}
fn.__get__(1, 2)
fn.__set__(1, 2)
fn.__delete__(1)
fn.__call__(1, 2, 3)
fn.__prepare__('foo', 'bar')
fn.__init_subclass__()
fn.__new__(1, 2, 3)
fn.__init__(1, 2, 3)
fn.__del__()
fn.__repr__()
fn.__str__()
fn.
