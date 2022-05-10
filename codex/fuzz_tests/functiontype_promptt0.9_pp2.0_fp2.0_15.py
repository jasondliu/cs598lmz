import types
# Test types.FunctionType and types. BuiltinFunctionType
class A:
    def __init__(self):
        self.id = id
    def __call__(self, o):
        return o

assert isinstance(A, types.FunctionType)
assert isinstance(A().id, types.BuiltinFunctionType)
assert isinstance(A().__call__, types.FunctionType)

# Test types.BuiltinMethodType
a = A()
assert isinstance(a.id, types.BuiltinMethodType)
assert isinstance(a.__call__, types.MethodType)
assert isinstance(a.__init__, types.MethodType)

# Test types.MethodType
def universal_method(*args, **kw):
    return args, kw

bound = universal_method.__get__(2, 3)
assert isinstance(bound, types.MethodType)

assert bound() == ((2,), {})
assert bound(1, 2) == ((2, 1, 2), {})
assert bound(1, 2, x=3) == ((2, 1, 2), {
