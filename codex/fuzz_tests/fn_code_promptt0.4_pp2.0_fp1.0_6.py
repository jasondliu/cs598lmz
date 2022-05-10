fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = "test.py"
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ("a", "b")
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount = 0
# Test fn.__code__.co_posonlyargcount
fn.__code__.co_posonlyargcount = 0
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2, 3)
# Test fn.__code__.co_names
fn.__code__.co_names = ("a", "b", "c")
