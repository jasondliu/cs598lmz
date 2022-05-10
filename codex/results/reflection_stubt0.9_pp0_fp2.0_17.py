fn = lambda: None
gi = (i for i in ())
fn.__code__ = c
gi.gi_code = c
del c, tb_fn, tb_fn2, tb_genexpr, tb_genexpr2, tb_cell, tb_cell2
del gi
fb = type(FrameType())(fn)
# End

# Start again
fn = lambda: None
new_code = PyCode_New(
    0, 0, 0, 0,
    0,
    fn.__code__.co_cellvars + (CELLVAR_NAME,),
    fn.__code__.co_freevars + (FREEVAR_NAME,),
    fn.__code__.co_code,
    fn.__code__.co_consts,
    fn.__code__.co_names,
    fn.__code__.co_varnames,
    fn.__code__.co_filename,
    fn.__code__.co_name,
    fn.__code__.co_firstlineno,
    fn.__code__.co_lnotab,
    fn.__code__
