fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(gi.gi_code)()
fn.__code__.co_filename = '<string>'
fn.__code__.co_firstlineno = 0
fn.__code__.co_argcount = 0
fn.__code__.co_flags = 0x20
fn.__code__.co_consts = (None,)
fn.__code__.co_code = b'\x00\x00\x00\x00'
fn.__code__.co_cellvars = ()
fn.__code__.co_freevars = ()
fn.__code__.co_nlocals = 0
fn.__code__.co_name = '<lambda>'
fn.__code__.co_names = ()
fn.__code__.co_varnames = ()
fn.__code__.co_stacksize = 0
fn.__code__.co_lnotab = b''

# We need our own version of types.CodeType
def _make_code(co):
    try:
        return types.CodeType(

