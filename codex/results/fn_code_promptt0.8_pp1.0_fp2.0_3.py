fn = lambda: None
# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount
getcode(print).co_varnames
getcode(fn).co_varnames
def fn(arg1, arg2, *args):
    x = 1
getcode(fn).co_varnames
getcode(fn).co_argcount
 
# Test fn.__code__.co_cellvars
# Test fn.__code__.co_freevars
def fn(arg1):
    def nested():
        return arg1 
getcode(fn).co_cellvars
getcode(fn).co_freevars
 
# Test fn.__code__.co_names
def fn():
    x = 1
getcode(fn).co_names
 
# Test fn.__code__.co_nlocals
getcode(fn).co_nlocals
 
# Test fn.__code__.co_stacksize
getcode(fn).co_stacksize
 
# Test fn.__code__.co_flags
getcode(fn
