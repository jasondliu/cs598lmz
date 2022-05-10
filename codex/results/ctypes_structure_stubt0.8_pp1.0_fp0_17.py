import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [('y', ctypes.c_int), ]

class D(S):
    pass

for k, v in D.__dict__.items():
    print k, v

class A:
    x = 1
    pass

class B(A):
    def __getattribute__(self, name):
        print 'getattribute(%s)' % name
        return type.__getattribute__(self, name)

    def __getattr__(self, name):
        print 'getattr(%s)' % name
        return type.__getattr__(self, name)

    def __setattr__(self, name, value):
        print 'setattr(%s, %s)' % (name, value)
        type.__setattr__(self, name, value)


class C(B):
    pass

c = C()
c.x = 2
print c.x

for i in range(10):
    print i

del i
try:
    print i
except NameError, detail:
    print
