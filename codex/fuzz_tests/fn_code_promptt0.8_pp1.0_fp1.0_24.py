fn = lambda: None
# Test fn.__code__.co_varnames
def f1(a,b,c):
    return f2(a)
f1._mt_test_fn.__code__.co_varnames = (1,2,3,4,5)
f2._mt_test_fn.__code__.co_varnames = (1,2,3,4,5)
f2._mt_test_fn.__code__.co_argcount = 4

# Test fn.__code__.co_argcount
def f1(a,b,c):
    return f2(a)
f2._mt_test_fn.__code__.co_argcount = 10

# Test fn.__code__.co_flags
def f1(a,b,c):
    return f2(a)
f1._mt_test_fn.__code__.co_flags = 1

# Test fn.__code__.co_cellvars
def f1(a,b,c):
    def f11():
        return x
    x = 10
    return
