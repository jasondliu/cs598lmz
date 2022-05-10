fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# test_code_co_freevars
def fn():
    a = 1
    def fn():
        print(a)
    return fn
fn()()

# test_code_co_names
def fn():
    a = 1
    def fn():
        print(a)
    return fn
fn()()

# test_code_co_varnames
def fn():
    a = 1
    def fn():
        print(a)
    return fn
fn()()

# test_code_co_argcount
def fn(a, b):
    print(a, b)
fn(1, 2)

# test_code_co_kwonlyargcount
def fn(a, *, b):
    print(a, b)
fn(1, b=2)

# test_code_co_nlocals
def fn():
    a = 1
    def fn():
        print(a)
    return fn
fn()()

# test_code_co_stacksize
def
