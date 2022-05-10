import types
# Test types.FunctionType and instancemethod

import types

def f(): pass
x = f
assert type(x) is types.FunctionType
assert not isinstance(x, types.MethodType)
assert not isinstance(x, types.ClassType)

#Methods are also functions, but with an im_self
class C:
    def f(self): pass
c = C()
x = c.f
assert type(x) is types.MethodType
assert isinstance(x, types.FunctionType)
assert not isinstance(x, types.ClassType)

#Classes are also functions, but with an __name__
class C:
    def f(self): pass
x = C
assert type(x) is types.ClassType
assert isinstance(x, types.FunctionType)
assert not isinstance(x, types.MethodType)

print 'OK'
