fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__code__.__class__(
    co_argcount=gi.gi_frame.f_code.co_argcount,
    co_kwonlyargcount=gi.gi_frame.f_code.co_kwonlyargcount,
    co_nlocals=gi.gi_frame.f_code.co_nlocals,
    co_stacksize=gi.gi_frame.f_code.co_stacksize,
    co_flags=gi.gi_frame.f_code.co_flags,
    co_code=b'',
    co_consts=(),
    co_names=(),
    co_varnames=(),
    co_filename=gi.gi_frame.f_code.co_filename,
    co_name=gi.gi_frame.f_code.co_name,
    co_firstlineno=gi.gi_frame.f_code.co_firstlineno,
    co_lnotab=b'',
    co_freevars=(),
    co_cellvars=()
)

