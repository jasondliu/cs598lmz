import types
# Test types.FunctionType, which is properly replaced by Cython even
# when used inside an if statement.
def test_function_type(arg):
    if isinstance(arg, types.FunctionType):
        return arg()
    return None

def my_function():
    return "OK"

result = test_function_type(types.FunctionType(my_function.__code__, {}, my_function.__name__))
assert result == "OK"
# Test weakref.ReferenceType, which is properly replaced by Cython even
# when used inside an if statement.
def test_weakref_referencetype(arg):
    if isinstance(arg, weakref.ReferenceType):
        return "OK"
    return None

r = weakref.ref(my_function)
result = test_weakref_referencetype(r)
assert result == "OK"
# Test types.MethodType, which is properly replaced by Cython even
# when used inside an if statement.
def test_method_type(arg):
    if isinstance(arg, types.MethodType):
        return
