import types
# Test types.FunctionType
import sys

def same(a, b):
    return type(a) is type(b)


class A:
    pass


pa = A()
pa.__class__ = types.FunctionType
if not same(pa.__call__, A.__call__.__get__(pa)):
    raise TypeError()

res = A.__call__.__get__(pa)()
if not isinstance(res, A):
    raise TypeError

pa.__class__ = int
if not same(pa.__trunc__, int.__trunc__.__get__(pa)):
    raise TypeError()

res = int.__trunc__.__get__(pa)()
if res != pa:
    raise TypeError

# Legacy class
# class B:
#     def foo(self): pass
#
# pb = B()
# pb.__class__ = types.FunctionType
#
# if not same(pb.foo, B.foo.__get__(pb)):
#     raise TypeError()
#

