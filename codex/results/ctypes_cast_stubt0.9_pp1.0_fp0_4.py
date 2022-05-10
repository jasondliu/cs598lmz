import ctypes
ctypes.cast(0, type(None))


# gets
class C(object):
    def __get__(self, inst, cls):
        pass

class D(object):
    x = C()
    x

D.__dict__['x'].__get__(1, D)


# classmethods
class C(object):
    @classmethod
    def f(cls):
        pass

    g = classmethod(f)

C.f
C.g
C.f is C.g

# staticmethods
class C(object):
    @staticmethod
    def f():
        pass

    g = staticmethod(f)

C.f
C.g
C.f is C.g

# properties
class C(object):
    @property
    def f(self):
        pass
    
    g = property(f)

C().f
C().g

# descriptors w/o __get__
class C(object):
    f = 1

C.f, C().f

def f(self):

