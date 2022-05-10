import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    pass

c_inst = C()
c_inst.x = 123

setattr(c_inst, 'y', 456)

print(c_inst.x, c_inst.y)

c = c_inst.x + 5
print(c)

CField = C.x
print(CField)

C.z = CField(1)
print(C.z)
