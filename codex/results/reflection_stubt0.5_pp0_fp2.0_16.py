fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #28861: check that the __code__ attribute of a built-in function
# is not writable.
def check_readonly(fn, attrname):
    with raises(TypeError):
        setattr(fn, attrname, None)

check_readonly(len, "__code__")
check_readonly(len, "__defaults__")
check_readonly(len, "__kwdefaults__")

# Issue #29429: check that we can get the code object of a built-in
# function even if its module has been deleted.
import builtins
del builtins.__dict__['len']
assert hasattr(len, '__code__')

# Issue #29429: check that a function's module is not set to None
# when its code object is deleted.
del len.__code__
assert len.__module__ != None

# Issue #29429: check that the __code__ attribute of a built-in
# function can be deleted.
del len.__code__

# Issue #29429
