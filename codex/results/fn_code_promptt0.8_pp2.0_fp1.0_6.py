fn = lambda: None
# Test fn.__code__.co_firstlineno
class A(object):
    def a(self): return 1

assert A.a.__code__.co_firstlineno == fn.__code__.co_firstlineno + 1
# Test fn.__code__.co_argcount
def f(): pass
assert f.__code__.co_argcount == 0
def f(arg): pass
assert f.__code__.co_argcount == 1
def f(arg1, arg2): pass
assert f.__code__.co_argcount == 2
def f(arg1, arg2, *args): pass
assert f.__code__.co_argcount == 2
def f(arg1, arg2, **kwargs): pass
assert f.__code__.co_argcount == 2
def f(arg1, arg2, *args, **kwargs): pass
assert f.__code__.co_argcount == 2
def f(*args): pass
assert f.__code__.co_argcount == 0
def f(**kwargs): pass
assert f.__code__
