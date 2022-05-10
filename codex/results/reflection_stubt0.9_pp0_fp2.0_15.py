fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.send.__code__

# Construct a METH_FASTCALL-like fake code object.
# The called function should have one STR parameter, or two STR
# parameters, or one unicode parameter, or two unicode parameters.
# The called function must return the length of its string argument
fn.__code__.co_varnames = ('a', 'b', 'c')
fn.__code__.co_argcount = 3
fn.__code__.co_cellvars = ()
fn.__code__.co_consts = (None, None, None, None, None,
                         100, (1, 2, 3), 2, 1, 2, fn.__code__)
# These magic numbers are:
# * METH_FASTCALL (0x80) | METH_VARARGS (0x4),
# * The index of the called function in co_consts,
# * The index of the encoding in co_consts,
# * The index of the size in co_consts,
fn.__code__.co_flags = 0x
