import types
# Test types.FunctionType type. 
print(types.FunctionType)

# See if a class-derived object derives from a special type.
class Foo:
    pass

print( issubclass(Foo, types.TypeType ))
print( issubclass(Foo, types.BuiltinFunctionType ))

# Create a function.
def gen():
    pass

print( issubclass(gen, types.TypeType))

print( issubclass(gen, types.BuiltinFunctionType))
