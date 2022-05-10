import types
# Test types.FunctionType
def f():
    pass

def g():
    pass

assert type(f) is types.FunctionType
assert type(g) is types.FunctionType
assert type(f) == type(g)

# Test types.LambdaType
l = lambda x: x

assert type(l) is types.LambdaType
assert type(l) != type(f)

# Test types.GeneratorType
g = (x for x in range(3))

assert type(g) is types.GeneratorType
assert type(g) != type(f)
assert type(g) != type(l)

# Test types.MethodType
class C:
    def m(self):
        pass

assert type(C.m) is types.MethodType
assert type(C().m) is types.MethodType
assert type(C.m) != type(f)
assert type(C.m) != type(l)
assert type(C.m) != type(g)
assert type(C().m) != type(f)
assert type(C().m
