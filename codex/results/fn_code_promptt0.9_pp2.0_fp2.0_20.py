fn = lambda: None
# Test fn.__code__.co_code
fn.func_code.co_code
# Test fn.__code__.co_varnames
fn.func_code.co_varnames
# Test fn.__code__.co_argcount
fn.func_code.co_argcount
# Test fn.__code__.co_consts
fn.func_code.co_consts

# test fn.__code.co_filename
fn.func_code.co_filename

# Test fn.__code.co_name
fn.func_code.co_name

f = 1
# Test f.__call__()
f.__call__()

# Test issue 3933
f = 1
bytearray()


# Test issue 3935
def fn(a, b):
    yield a + b

a = fn()
a.gi_frame
a.gi_frame.f_locals
# Test issue 3967
if True:
    # Test nested-class method b
    class A(object):
        class B(object):
            def c(self): pass
