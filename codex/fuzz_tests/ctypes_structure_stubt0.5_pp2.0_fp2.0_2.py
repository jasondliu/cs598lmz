import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    __slots__ = ['x', 'z']

s = S()
print(dir(s))
s.x = 1
s.y = 2
s.z = 3
print(s.x, s.y, s.z)
print(s.y)
</code>
Output:
<code>['__class__', '__ctypes_from_outparam__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__sub
