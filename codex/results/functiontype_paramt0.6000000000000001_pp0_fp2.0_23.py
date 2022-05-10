from types import FunctionType
list(FunctionType(lambda x: x, globals())(x) for x in range(10))

# Function type is an immutable type, so it has no attributes
# FunctionType(lambda x: x, globals()).foo = 'bar'

# FunctionType is not a subtype of type
# isinstance(lambda x: x, type)

# FunctionType is a subtype of object
# isinstance(lambda x: x, object)

# FunctionType is a subclass of object
# issubclass(FunctionType, object)

# FunctionType is a subclass of type
# issubclass(FunctionType, type)

# FunctionType is not a subclass of int
# issubclass(FunctionType, int)

# FunctionType is not a subclass of str
# issubclass(FunctionType, str)

# FunctionType is not a subclass of bool
# issubclass(FunctionType, bool)

# FunctionType is not a subclass of list
# issubclass(FunctionType, list)

# FunctionType is not a subclass of dict
# issubclass(FunctionType, dict)

# Function
