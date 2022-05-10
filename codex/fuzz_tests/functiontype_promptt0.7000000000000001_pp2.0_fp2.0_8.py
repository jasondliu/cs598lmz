import types
# Test types.FunctionType

def f1(x):
    return x

class C(object):
    def f2(self, x):
        return x

c = C()

print f1, type(f1)
print c.f2, type(c.f2)
print f1(42), c.f2(42)

# FunctionType is a type object
print isinstance(f1, types.FunctionType)
print isinstance(c.f2, types.FunctionType)

# FunctionType is also a class object
print issubclass(types.FunctionType, object)

# FunctionType is an instance of type
print isinstance(types.FunctionType, type)

# FunctionType is a subclass of type
print issubclass(types.FunctionType, type)
