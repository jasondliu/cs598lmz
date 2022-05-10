fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__module__ = '__main__'
fn.__qualname__ = '<lambda>'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = None
fn.__dict__ = {}
fn.__doc__ = None
fn.__text_signature__ = None

# The following code is used to make `fn` a function that raises an exception
# when called.
#
# The code is taken from the `inspect` module.
fn.__code__.co_argcount = 0
fn.__code__.co_cellvars = ()
fn.__code__.co_code = b'|\x00|\x01\x17\x00S\x00'
fn.__code__.co_consts = (None,)
fn.__code__.co_filename = '<lambda>'
fn.__code__.co_
