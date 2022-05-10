fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_is_not_callable
def f(): pass
f.__code__ = 1
try:
    f()
except TypeError:
    pass
else:
    raise Exception

# test_code_is_not_mapping
def f(): pass
f.__code__ = 1
try:
    f.__code__["co_argcount"]
except TypeError:
    pass
else:
    raise Exception

# test_code_is_not_sequence
def f(): pass
f.__code__ = 1
try:
    f.__code__[0]
except TypeError:
    pass
else:
    raise Exception

# test_code_is_readonly
def f(): pass
try:
    f.__code__ = 1
except TypeError:
    pass
else:
    raise Exception

# test_code_argcount_is_readonly
def f(): pass
try:
    f.__code__.co_argcount = 1
except AttributeError:
    pass
else:

