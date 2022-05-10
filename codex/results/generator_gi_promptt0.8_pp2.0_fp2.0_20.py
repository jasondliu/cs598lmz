gi = (i for i in ())
# Test gi.gi_code.
# gi.gi_code is a builtin method '__iter__'
# The method must have __name__, __self__ and __code__ attributes.
import builtins
import types
assert hasattr(next(gi).__code__, 'co_firstlineno')
check_static_attr(builtins, 'TypeError', '__name__', str)
check_static_attr(builtins, 'TypeError', '__module__', str)
check_static_attr(types.MethodType, '__name__', str)
check_static_attr(types.MethodType, '__module__', str)
check_static_attr(types.MethodType, '__code__', types.CodeType)

# Test gi.gi_frame.
test_tuple = (1, 2, 3)
def test_func():
    return test_tuple[0]

def test_func2():
    return test_func()

def test_func3():
    return test_func2()

assert test_func3() == 1

assert hasattr(test
