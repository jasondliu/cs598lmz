fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_invalid_freevars
def fn():
    fn.__code__.co_freevars = (1, 2, 3)
fn()

# test_code_invalid_cellvars
def fn():
    fn.__code__.co_cellvars = (1, 2, 3)
fn()

# test_code_invalid_name
def fn():
    fn.__code__.co_name = 1
fn()

# test_code_invalid_argcount
def fn():
    fn.__code__.co_argcount = -1
fn()

# test_code_invalid_kwonlyargcount
def fn():
    fn.__code__.co_kwonlyargcount = -1
fn()

# test_code_invalid_nlocals
def fn():
    fn.__code__.co_nlocals = -1
fn()

# test_code_invalid_stacksize
def fn():
    fn.__code__.co_stacks
