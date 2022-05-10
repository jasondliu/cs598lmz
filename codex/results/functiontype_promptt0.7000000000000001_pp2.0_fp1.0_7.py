import types
# Test types.FunctionType
def f(): pass
if not isinstance(f, types.FunctionType):
    print("FunctionType failed", f)

# Test types.MethodType
class A:
    def m(self): pass
x = A()
if not isinstance(x.m, types.MethodType):
    print("MethodType failed", x.m)

# Test types.BuiltinMethodType
class B:
    def m(self): pass
b = B()
if not isinstance(b.m, types.BuiltinMethodType):
    print("BuiltinMethodType failed", b.m)

# Test types.LambdaType
l = lambda: None
if not isinstance(l, types.LambdaType):
    print("LambdaType failed", l)

# Test types.GeneratorType
g = (x for x in [1,2,3])
if not isinstance(g, types.GeneratorType):
    print("GeneratorType failed", g)

# Test types.GeneratorType
g = (x for x in [1,2,3])

