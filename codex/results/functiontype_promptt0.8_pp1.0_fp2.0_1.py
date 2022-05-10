import types
# Test types.FunctionType with argument checking

def f(): pass

# A FunctionType that does not accept any arguments at all
class NoArgs(object):
    def __call__(self): pass

def test_FunctionType(func, *args):
    try:
        func()
    except TypeError: # Python 2.x
        pass
    except SystemError: # Python 3.x
        pass
    else:
        raise RuntimeError('should have raised')
    try:
        func(None)
    except TypeError:
        pass
    else:
        raise RuntimeError('should have raised')
    try:
        func(*args)
    except TypeError:
        raise RuntimeError('should not have raised')

test_FunctionType(f)
test_FunctionType(f, 0)
test_FunctionType(f, 0, 1)
test_FunctionType(f, 1, 2, 3)

test_FunctionType(NoArgs())
test_FunctionType(NoArgs(), None)
test_FunctionType(NoArgs(), None, None)
test_FunctionType(NoArgs(), None, None,
