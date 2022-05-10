from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Descriptors
class C(object):
    def __get__(self, obj, type=None):
        return 1

class D(object):
    x = C()

D.x
D().x

# Slots
class C(object):
    __slots__ = ['x']

C.x
C().x

# Old-style classes
class C:
    def __getattr__(self, name):
        return 1

C.x
C().x

# Properties
class C(object):
    @property
    def x(self):
        return 1

C.x
C().x

# __getattr__
class C(object):
    def __getattr__(self, name):
        return 1

C.x
C().x

# __getattribute__
class C(object):
    def __getattribute__(self, name):
        return 1

C.x
C().x

# __get__
