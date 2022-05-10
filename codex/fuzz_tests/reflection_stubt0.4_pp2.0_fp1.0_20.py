fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_new_empty_code
code = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# test_code_new_normal_code
def func(a, b, c):
    pass

code = types.CodeType(0, 0, 0, 0, b'', (), ('a', 'b', 'c'), (), 'func', 'funcfile', 1, b'')

# test_code_new_negative_lineno
def func():
    pass

code = types.CodeType(0, 0, 0, 0, b'', (), (), (), 'func', 'funcfile', -1, b'')

# test_code_new_too_many_freevars
def func():
    pass

code = types.CodeType(0, 0, 0, 0, b'', (), (), (), 'func', 'funcfile', 1, b'\x00' * 256)

# test_code_new_too_many_kwonlyargs
def func
