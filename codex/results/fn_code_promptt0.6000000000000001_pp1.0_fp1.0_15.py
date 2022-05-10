fn = lambda: None
# Test fn.__code__
fn.__code__ = sys._getframe(0).f_code
# Test fn.__code__.co_name
fn.__code__.co_name = "foo"
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ("bar", "baz")
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 42
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 0
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 0
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 0
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = ""
# Test fn.__code__.co_names
fn.__
