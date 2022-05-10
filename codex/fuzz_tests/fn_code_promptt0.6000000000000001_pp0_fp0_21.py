fn = lambda: None
# Test fn.__code__.co_filename
setattr(fn, "__code__", lambda:None)
fn.__code__.co_filename = "test.py"
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 42
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ("a", "b")
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ("c", "d")
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ("e", "f")
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_consts
fn.__code__.co_consts = (None,)
# Test fn.__code__.co_names
fn.
