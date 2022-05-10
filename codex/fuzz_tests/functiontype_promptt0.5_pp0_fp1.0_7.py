import types
# Test types.FunctionType()
def test():
    print("Test!")

r = types.FunctionType(test.__code__, test.__globals__, name=test.__name__,
                  argdefs=test.__defaults__, closure=test.__closure__)
r()

# Test types.MethodType()
class A:
    def __init__(self, v):
        self.v = v
    def test(self):
        print("test: %d" % self.v)

a = A(10)
a.test()

m = types.MethodType(a.test.__func__, a)
m()

# Test types.BuiltinFunctionType()
print(abs)
print(types.BuiltinFunctionType(abs))

# Test types.BuiltinMethodType()
print(list.append)
print(types.BuiltinMethodType(list.append))

# Test types.ModuleType()
m = types.ModuleType("test")
print(m)

# Test types.TracebackType()
try:
    raise
