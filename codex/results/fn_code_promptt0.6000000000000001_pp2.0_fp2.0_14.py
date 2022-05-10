fn = lambda: None
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ("a",)
# Test fn.__code__.co_name
fn.__code__.co_name = "foo"
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b"ab"
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ("b",)
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ("c",)

# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, None, type(fn.__code__))

# Test fn.__code__.co_stacksize
fn.__code__.
