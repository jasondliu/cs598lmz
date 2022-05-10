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
class E(object):
    __slots__ = ['x']

E().x = 1

# Subclasses
class F(object):
    pass

class G(F):
    pass

G()

# Multiple inheritance
class H(object):
    pass

class I(object):
    pass

class J(H, I):
    pass

J()

# Extension classes
class K(object):
    pass

K()

# Old-style classes
class L:
    pass

L()

# Metaclasses
class M(type):
    pass

class N(object):
    __metaclass__ = M

N()

# __import__
__import__('os')

# Import hooks

