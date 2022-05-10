import types
# Test types.FunctionType (values must be instances of types.FunctionType)
@njit
def fn_boo():
    return 3

def test_fn_boo():
    return fn_boo

@njit
def fn_foo1():
    # No error
    fn = test_fn_boo()
    return fn()

@njit
def fn_foo2():
    # No error
    fn = test_fn_boo()
    return fn

@njit
def fn_foo3():
    # TypeError: test_fn_boo() not supported inside jitted functions
    fn = test_fn_boo()
    return test_fn_boo()

@njit
def fn_foo4():
    # No error
    fn = types.FunctionType
    return fn

@njit
def fn_foo5():
    # TypeError: FunctionType not supported inside jitted functions
    fn = test_fn_boo()
    return fn.__code__

@njit
def fn_foo6():
    # No error
    fn =
