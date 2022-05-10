fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
 
# call_function
def fn():
    return
fn.__code__ = getattr(fn, '__code__', None)
fn()
 
# call_function_var
def fn(a, b, c):
    return
fn.__code__ = getattr(fn, '__code__', None)
fn(1, 2, 3)
 
# call_function_kw
def fn(a, b, c):
    return
fn.__code__ = getattr(fn, '__code__', None)
dict1 = {'a': 1, 'b': 2, 'c': 3}
fn(**dict1)
 
# call_function_kw_var
def fn(a, b, c, d):
    return
fn.__code__ = getattr(fn, '__code__', None)
dict1 = {'a': 1, 'b': 2, 'c': 3}
fn(d=4, **dict1)
 
# call_function_var_kw
def fn(a
