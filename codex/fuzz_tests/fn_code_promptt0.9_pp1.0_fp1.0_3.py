fn = lambda: None
# Test fn.__code__
fn.__code__.co_argcount
assert fn.__code__.co_code
fn.__code__.co_consts
fn.__code__.co_filename
fn.__code__.co_firstlineno
fn.__code__.co_flags
fn.__code__.co_freevars
fn.__code__.co_lnotab
fn.__code__.co_name
# Test .co_names
{
    ns.__main__: None,
    "sys": None,
    "os": None,
    "__builtins__": None,
    "PyQt4": None
}.get(fn.__code__.co_names)
fn.__code__.co_namespace
# Test .co_nlocals
fn.__code__.co_nlocals == 0
fn.__code__.co_stacksize
fn.__code__.co_varnames
