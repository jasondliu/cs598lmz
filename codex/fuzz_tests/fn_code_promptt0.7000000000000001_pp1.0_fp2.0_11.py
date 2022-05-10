fn = lambda: None
# Test fn.__code__
def fn(x, y): pass
fn.__code__
fn.__code__.co_argcount
fn.__code__.co_varnames
fn.__code__.co_name
fn.__code__.co_filename
fn.__code__.co_flags
fn.__code__.co_firstlineno
fn.__code__.co_lnotab
fn.__code__.co_consts
fn.__code__.co_names
fn.__code__.co_stacksize
fn.__code__.co_code
# Test fn.__defaults__
def fn(x, y=1): pass
fn.__defaults__
# Test fn.__kwdefaults__
def fn(x, y=1, *args, z=1, **kwargs): pass
fn.__kwdefaults__
# Test fn.__globals__
def fn(): pass
fn.__globals__
# Test fn.__closure__
def fn(): pass
fn.__closure__
def fn():
    a = 1
   
