fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)(
    co_argcount=0, co_kwonlyargcount=0, co_nlocals=0, co_stacksize=2,
    co_flags=67, co_code=b'c\x00\x00S\x00', co_consts=(None,),
    co_names=(), co_varnames=(), co_filename='', co_name='',
    co_firstlineno=1, co_lnotab=b'\x00\x01', co_freevars=(), co_cellvars=())
fn.__defaults__ = ()
fn.__kwdefaults__ = None

# These are used in various tests
def f0(*args): pass
def f1(a): pass
def f2(a, b): pass
def f3(a, b, c): pass
def f4(a, b, c, d): pass
def f5(a, b, c, d, e): pass
def f6(a, b, c, d,
