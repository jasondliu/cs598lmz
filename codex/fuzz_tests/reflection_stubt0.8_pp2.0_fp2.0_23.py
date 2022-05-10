fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn.__code__ = 42
except TypeError:
    pass
else:
    raise ValueError("shouldn't be able to assign int to __code__")
try:
    fn.__code__ = []
except TypeError:
    pass
else:
    raise ValueError("shouldn't be able to assign list to __code__")
try:
    fn.__code__ = {}
except TypeError:
    pass
else:
    raise ValueError("shouldn't be able to assign dict to __code__")
code = fn.__code__
code = code
code.co_varnames = (1, 2, 3)
try:
    code.co_varnames = 'abc'
except TypeError:
    pass
else:
    raise ValueError("shouldn't be able to assign string to co_varnames")
try:
    code.co_varnames = ['a', 'b', 'c']
except TypeError:
    pass
else:
    raise ValueError("shouldn't be able to assign list to co_v
