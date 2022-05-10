fn = lambda: None
# Test fn.__code__.co_argcount
#@this_fails_on_py3
def co_argcount_test():
    def f(): pass
    assert f.__code__.co_argcount == 0
    def g(x): return x
    assert g.__code__.co_argcount == 1
    def h(x, y): return x, y
    assert h.__code__.co_argcount == 2

# Test fn.__code__.co_flags
#@this_fails_on_py3
def co_flags_test():
    def f(): pass
    assert f.__code__.co_flags == 0
    def g(x): return x + 1
    assert g.__code__.co_flags == 0
    def h(x, y): return x, y
    assert h.__code__.co_flags == 0

# Test fn.__code__.co_firstlineno
#@this_fails_on_py3
def co_firstlineno_test():
    def f(): pass
    assert f.__code__
