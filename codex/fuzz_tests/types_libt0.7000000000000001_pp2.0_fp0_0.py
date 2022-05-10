import types
types.MethodType(f, None, cls)
types.MethodType(f, None, cls)()
types.MethodType(f, None, cls)()

# This is the same as the previous one, but checks that the code is
# identical.

def f(self, x, y=42):
    print(x, y)

class cls:
    pass

m1 = types.MethodType(f, None, cls)
m2 = types.MethodType(f, None, cls)
print(m1.__code__ is m2.__code__)

# Make sure that we properly support the signature() builtin, see bpo-20585.
import inspect
print(inspect.signature(m1))
print(inspect.signature(m2))
