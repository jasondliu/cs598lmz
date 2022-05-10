fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_new_empty_code
# code_new_empty_code

def fn():
    pass

fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
fn()

# test_code_new_bad_argcount
# code_new_bad_argcount

def fn():
    pass

fn.__code__ = type(fn.__code__)(-1, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
fn()

# test_code_new_bad_kwonlyargcount
# code_new_bad_kwonlyargcount

def fn():
    pass

fn.__code__ = type(fn.__code__)(0, -1, 0, 0, b'', (), (), (), '', '', 0, b'')
fn()

# test_code_new_bad_nlocals
# code_new_bad_nlocals


