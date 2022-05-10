import types
# Test types.FunctionType
def fn():
    pass
assert isinstance(fn, types.FunctionType)

# Test types.MethodType
class A:
    def fn(self):
        pass
a = A()
assert isinstance(a.fn, types.MethodType)
