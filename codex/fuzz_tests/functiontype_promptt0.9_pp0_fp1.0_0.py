import types
# Test types.FunctionType
if type(f) is not types.FunctionType:
    print('FAILED!')
else:
    print('PASSED!')

# Test __name__
if f.__name__ != "f":
    print('FAILED!')
else:
    print('PASSED!')

# Test __module__
if f.__module__ != __name__:
    print('FAILED!')
else:
    print('PASSED!')

# Test __isabstractmethod__
if hasattr(f, "__isabstractmethod__"):
    print('FAILED!')
else:
    print('PASSED!')

## Test __self__
#if f.__self__ is not None:
#    print 'FAILED!'
#else:
#    print 'PASSED!'

# Test __call__
f()

# Test __get__
if callable(f.__get__("foo")):
    print('PASSED!')
else:
    print('FAILED!')

# Test from_param

