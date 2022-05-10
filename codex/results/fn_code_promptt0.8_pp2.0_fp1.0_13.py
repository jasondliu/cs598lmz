fn = lambda: None
# Test fn.__code__.co_argcount
def f1(a, b, c=42, d=43, e=44): pass
def f2(a, b, *args): pass
def f3(a, b, *args, **kwargs): pass
def f4(a, b, c=42, d=43, e=44, *args, **kwargs): pass
fn.__code__.co_argcount
fn.__code__.co_argcount = 42
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize
fn.__code__.co_stacksize = 42
# Test fn.__defaults__
def f1(a, b, c=42, d=43, e=44): pass
def f2(a, b, *args): pass
def f3(a, b, *args, **kwargs): pass
def f4(a, b, c=42, d=43, e=44, *args, **kwargs): pass
fn.__defaults__
fn.__defaults__ =
