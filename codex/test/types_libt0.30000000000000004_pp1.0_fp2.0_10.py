import types
types.MethodType(foo, None)

# Test that the builtin type() function works.
type(foo)

# Test that the builtin isinstance() function works.
isinstance(foo, types.FunctionType)
isinstance(foo, types.BuiltinFunctionType)
isinstance(foo, types.MethodType)

# Test that the builtin issubclass() function works.
issubclass(types.FunctionType, object)
issubclass(types.BuiltinFunctionType, object)
issubclass(types.MethodType, object)

# Test that the builtin callable() function works.
callable(foo)

# Test that the builtin super() function works.
super(object, object())

# Test that the builtin vars() function works.
vars(object())

# Test that the builtin dir() function works.
dir(object())

# Test that the builtin getattr() function works.
getattr(object(), '__doc__')

# Test that the builtin setattr() function works.
