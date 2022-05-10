import types
# Test types.FunctionType
def function(*args): pass
def _test():
    f = function
    return isinstance(f, types.FunctionType)

try:
    assert _test()
except:
    print('Traceback (most recent call last):')
    raise
