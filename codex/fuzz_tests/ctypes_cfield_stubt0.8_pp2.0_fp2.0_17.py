import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyFloat(ctypes.c_float):
    def __new__(cls, value):
        return super(MyFloat, cls).__new__(cls, round(value, 3))

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, super(MyFloat, self).__repr__())

# subclassing ctypes.CFloat to create a new ctypes Field type
# and override the __new__ and __repr__ methods
MyField = type(MyFloat())

class MyStructure(ctypes.Structure):
    _fields_ = [('a', MyField)]

m = MyStructure()
m.a = 1.2345
print(m.a) # 1.235
print(repr(m.a)) # MyFloat(1.234)
</code>
By subclassing ctypes.CFloat, you can do anything to your new subclass.

