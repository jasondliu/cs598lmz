import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def foo(self):
        pass

c = C()
c.foo = S.x

class D(C):
    def bar(self):
        pass

d = D()
d.foo = S.x
d.bar = S.x

print c.foo
print d.foo
print d.bar
</code>

