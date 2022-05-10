fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = "foo"
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = "foo"
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ("foo",)
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ("foo",)
