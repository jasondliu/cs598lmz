import types
types.MethodType(lambda self, x: x, None)

# This is a function, not a method
types.FunctionType(lambda x: x, globals())

# A built-in function is still a function
types.BuiltinFunctionType(len)

# A built-in method is a special case of method
types.BuiltinMethodType(str.replace)

# Methods are a subtype of function
issubclass(types.MethodType, types.FunctionType)

# But not vice versa
issubclass(types.FunctionType, types.MethodType)

# Classes are not functions
issubclass(type, types.FunctionType)

# Neither are instances
issubclass(object, types.FunctionType)

# Methods are not classes
issubclass(types.MethodType, type)

# Functions are not classes
issubclass(types.FunctionType, type)

# And no, instances are not classes either
issubclass(object, type)

# But everything is an instance of something
isinstance(len, object)

# Except for classes themselves
isinstance
