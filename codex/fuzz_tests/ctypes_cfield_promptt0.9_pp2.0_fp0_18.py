import ctypes
# Test ctypes.CField class

class S(ctypes._SimpleCData):
    _type_ = "i"
    pass
class C(ctypes._CData):
    _fields_ = [("i", S)]

c1 = C()
c2 = c1.i
assert ischaracter(c1), repr(type(c1))
assert ischaracter(c2), repr(type(c2))
print c2._objects.values()
assert list(c2._objects.values()) == [c1]
c2.value = 3
assert c1.i.value == 3
print 'done'
