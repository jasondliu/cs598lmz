fn = lambda: None
# Test fn.__code__.co_nlocals
#
def test_fn():
    x = 1
    y = 2
    z = 3
    return x + y + z

def test_fn_co_nlocals():
    print(test_fn.__code__.co_nlocals)

test_fn_co_nlocals()

# Test fn.__code__.co_varnames
#
def test_fn_co_varnames():
    print(test_fn.__code__.co_varnames)

test_fn_co_varnames()

# Test fn.__code__.co_argcount
#
def test_fn_co_argcount():
    print(test_fn.__code__.co_argcount)

test_fn_co_argcount()

# Test fn.__code__.co_cellvars
#
def test_fn_co_cellvars():
    a = 1
    b = 2
    c = 3
    def inner_fn():
        nonlocal a
        nonlocal b
