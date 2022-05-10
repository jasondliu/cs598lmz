fn = lambda: None
# Test fn.__code__
fn.__code__
fn.__code__.co_argcount
fn.__code__.co_varnames
fn.__code__.co_cellvars
fn.__code__.co_freevars
fn.__code__.co_consts
fn.__code__.co_names
fn.__code__.co_firstlineno
# Test fn.__defaults__
fn.__defaults__
fn.__kwdefaults__
# Test fn.__closure__
fn.__closure__
# Test fn.__annotations__
fn.__annotations__
fn.__dict__
fn.__globals__
fn.__name__
fn.__qualname__
fn.__text_signature__
fn.__module__

# Test fn.__get__
fn.__get__
fn.__get__(None, None)
fn.__get__(None, type(None))
fn.__get__(1, int)
fn.__get__(1.0, float)
fn.__get__("", str)
