fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: 0)()
fn.__code__.co_firstlineno = gi.gi_code.co_firstlineno = 1
fn.__code__.co_filename = gi.gi_code.co_filename = "test"

# This can't happen with CPython:
#   TypeError: can't set attributes of built-in/extension type 'code'
try:
    fn.__code__.co_varnames = ("a", "b")
except TypeError:
    pass


def f():
    pass


fn1 = f
gi1 = (i for i in ())
fn1.__code__ = gi1.gi_code
fn1.__code__.co_firstlineno = gi1.gi_code.co_firstlineno = 1
fn1.__code__.co_filename = gi1.gi_code.co_filename = "test"

# This can't happen with CPython:
#   TypeError: can't set attributes of built-in/extension type 'code
