import types
# Test types.FunctionType

def f(): pass

# FunctionType is a subclass of type
assert issubclass(types.FunctionType, type)

# FunctionType is a type
assert isinstance(f, types.FunctionType)

# FunctionType instance has a __name__ attribute
assert f.__name__ == "f"

# FunctionType instance has a __qualname__ attribute
assert f.__qualname__ == "f"

# FunctionType instance has a __annotations__ attribute
assert f.__annotations__ == {}

# FunctionType instance has a __doc__ attribute
assert f.__doc__ == None

# FunctionType instance has a __module__ attribute
assert f.__module__ == __name__

# FunctionType instance has a __globals__ attribute
assert f.__globals__ == globals()

# FunctionType instance has a __dict__ attribute
assert f.__dict__ == {}

# FunctionType instance has a __closure__ attribute
assert f.__closure__ == None

# FunctionType instance has a __code__ attribute
assert isinstance(f.__code__
