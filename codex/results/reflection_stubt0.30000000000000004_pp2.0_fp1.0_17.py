fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_new_empty_freevars
fn = lambda: None
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
fn()

# test_code_new_empty_names
fn = lambda: None
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', ())
fn()

# test_code_new_empty_varnames
fn = lambda: None
fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', (), ())
fn()

# test_code_new_kwonlyargcount_negative
try:
    types.CodeType(0, 0, 0, -1, b'', (), (), (), '', '', 0, b'', (), (), ())
except ValueError:
    pass
else:
    print('ValueError expected')

# test
