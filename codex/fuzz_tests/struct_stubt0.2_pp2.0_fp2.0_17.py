from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# test __new__
class C(object):
    def __new__(cls, *args):
        return object.__new__(cls)

C()

# test __new__ with a tuple
class D(object):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)

D(1, 2, 3)

# test __new__ with a tuple and __init__
class E(object):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)
    def __init__(self, *args):
        pass

E(1, 2, 3)

# test __new__ with a tuple and __init__
class F(object):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)
    def __init__(self, *args):
        self.args = args

F(1,
