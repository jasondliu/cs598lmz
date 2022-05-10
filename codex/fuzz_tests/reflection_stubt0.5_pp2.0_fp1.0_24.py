fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the exception is raised
# when the code object has a non-empty
# co_varnames.
gi = (i for i in ())
gi.gi_code = type((lambda: None).__code__)(
    0,                # co_argcount
    0,                # co_kwonlyargcount
    0,                # co_nlocals
    0,                # co_stacksize
    0,                # co_flags
    b"",              # co_code
    (),               # co_consts
    (),               # co_names
    ("x",),           # co_varnames
    "<string>",       # co_filename
    "<genexpr>",      # co_name
    0,                # co_firstlineno
    b"",              # co_lnotab
    (),               # co_freevars
    (),               # co_cellvars
)

with pytest.raises(TypeError):
    gi()

# Test that the exception is raised
# when the code object has a non
