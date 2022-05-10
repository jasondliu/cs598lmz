fn = lambda: None
# Test fn.__code__.co_firstlineno

def bar():
    print(42)

def foo(fn):
    print(fn.__code__.co_firstlineno)  # line no. 3 = OK
    fn()

foo(bar)
# Test explicit locals

def bar():
    print(locals())

def clear_locals(fn):
    fn.__code__ = None
    fn.__code__ = fn.__code__  # very explicit

# skip this line, it's just an optimization in CPython
# ClearBlock(fn);

def modify_locals(fn):
    # TODO: fix this -- this should clear but not change the co_locals
    fn.__code__.co_locals = None
    fn.__code__.co_locals = fn.__code__.co_locals
    fn.__code__.co_locals = ('bar', 42)

# check that a clear locals has no locals
fn = bar
clear_locals(fn)
fn()  # {} = ok

# change the local
