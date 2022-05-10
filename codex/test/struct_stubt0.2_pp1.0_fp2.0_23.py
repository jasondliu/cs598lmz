from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# test __new__
class A(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

class B(A):
    def __init__(self, *args, **kwargs):
        pass

B()

# test __new__ with __init__
class A(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    def __init__(self, *args, **kwargs):
        pass

class B(A):
    pass

B()

# test __new__ with __init__
class A(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    def __init__(self, *args, **kwargs):
        pass

