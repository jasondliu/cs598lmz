fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename = '<unknown>'
fn.__code__.co_firstlineno = 1
fn.__code__.co_lnotab = b'\x00\x01'
fn.__code__.co_code = b'x\x00\x00S'
fn.__code__.co_flags = 0
fn.__code__.co_names = ()
fn.__code__.co_varnames = ()
fn.__code__.co_freevars = ()
fn.__code__.co_cellvars = ()
fn.__code__.co_consts = (None,)
try:
    fn.__code__.co_stacksize = 1
except AttributeError:
    pass
try:
    fn.__code__.co_stacksize = 1
except AttributeError:
    pass
try:
    fn.__code__.co_stacksize = 1
except AttributeError:
    pass
try:
    fn.__code__.co_
