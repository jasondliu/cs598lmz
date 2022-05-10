import types
# Test types.FunctionType
def f(x): return  x
assert type(f) == types.FunctionType
# Test types.MethodType
class A:
    def f(self, x):
        return self, x
#
a = A()
af = A.f
mf = a.f
#
assert type(af) == types.MethodType
assert type(mf) == types.MethodType
assert type.mro(A) == [type, object]
# Test PyType_Ready
#
type.mro(A)
#
def test(x):
    if isinstance(x, A):
        return True
    return False
#
def new_test(x):
    if isinstance(x, A):
        return x.x
    return False
#
# Test PyHeapTypeObject
class H(type):
    pass
#
class C(object, metaclass=H):
    pass
#
class D(C):
    pass
#
assert type(C) is H
assert type.mro(D) == [D, C, object]
#
