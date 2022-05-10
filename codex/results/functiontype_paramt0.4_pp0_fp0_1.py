from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), "lambda_function")(0))

# FunctionType is a subclass of type
issubclass(FunctionType, type)

# classmethod is a subclass of FunctionType
issubclass(classmethod, FunctionType)

# staticmethod is a subclass of FunctionType
issubclass(staticmethod, FunctionType)

# property is a subclass of FunctionType
issubclass(property, FunctionType)

# object.__init__ is a FunctionType
isinstance(object.__init__, FunctionType)

# object.__new__ is a FunctionType
isinstance(object.__new__, FunctionType)

# object.__del__ is a FunctionType
isinstance(object.__del__, FunctionType)

# object.__repr__ is a FunctionType
isinstance(object.__repr__, FunctionType)

# object.__str__ is a FunctionType
isinstance(object.__str__, FunctionType)

# object.__bytes__ is a FunctionType
isinstance(object.__bytes__, FunctionType)

