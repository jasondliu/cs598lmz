from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i', 0)
s.pack(1)

# __getattribute__
class C(object):
    def __getattribute__(self, name):
        return 1

C().x

# __getattr__
class C(object):
    def __getattr__(self, name):
        return 1

C().x

# __get__
class C(object):
    def __get__(self, obj, type):
        return 1

C().x

# __call__
class C(object):
    def __call__(self, *args):
        return 1

C()()

# __init__
class C(object):
    def __init__(self, x):
        self.x = x

C(1)

# __new__
class C(object):
    def __new__(cls, x):
        self = object.__new__(cls)
        self.x = x
        return self

C(1)

