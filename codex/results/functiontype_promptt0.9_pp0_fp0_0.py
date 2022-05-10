import types
# Test types.FunctionType.  This also tests types.BuiltinFunctionType, but
# does not test most built-in functions.
assert type(pow) == types.BuiltinFunctionType
# pow() is a built-in function that has been shadowed by the math module
assert type(math.pow) == types.MethodType
try:
    r = pow(3, 4)
except NameError:
    raise TestFailed, 'pow() is not being shadowed by the math module'
else:
    assert r == 81

assert type(pow) == types.BuiltinFunctionType
def check_ClassMethodType(x):
    assert x.__name__ == 'classmethod'
    assert x.__dict__ == {'__doc__': 'classmethod(function) -> method\n\nConvert a function to be a class method.\n\nA class method receives the class as implicit first argument,\njust like an instance method receives the instance.\nTo declare a class method, use this idiom:\n\n  class C:\n      def f(cls, arg1, arg2, ...
