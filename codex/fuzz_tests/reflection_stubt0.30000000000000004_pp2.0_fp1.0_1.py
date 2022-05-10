fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_newempty
code = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# test_code_new
def func(a):
    b = a + 1
    return b

code = func.__code__

# test_code_new_badargs
try:
    types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', 0)
except TypeError:
    pass

try:
    types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', 0, 0)
except TypeError:
    pass

# test_code_new_kwargs
code = types.CodeType(co_argcount=0, co_kwonlyargcount=0, co_nlocals=0, co_stacksize=0, co_flags=0, co_code=b'', co_consts=(), co_names=(), co
