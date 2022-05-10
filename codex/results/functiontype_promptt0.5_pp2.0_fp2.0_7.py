import types
# Test types.FunctionType
def f(): pass
def g(): pass
def h(): pass

print(f.__code__)
print(type(f.__code__))
print(type(f.__code__.co_code))

print(type(f) is types.FunctionType)
print(type(lambda: None) is types.FunctionType)
print(type(f) is types.BuiltinFunctionType)
print(type(g) is types.BuiltinFunctionType)
print(type(h) is types.BuiltinFunctionType)

print(f.__code__ is g.__code__)
print(f.__code__ is h.__code__)

print(type(f) is type(g))
print(type(f) is type(h))

print(type(f) is type(lambda: None))

# Test types.MethodType
class C:
    def meth(self): pass

inst = C()
print(inst.meth)
print(inst.meth.__code__)
print(type(inst.meth.__code__
