import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldType = ctypes.CField.__class__

i = ctypes.c_int.in_dll(ctypes.pythonapi, "PyThreadState_Current")
print type(i), i, i.__class__, type(i.__class__), i.__class__ is type(i)
# <type '_ctypes.Field'> -238907248 <class '_ctypes._Field'> True

print type(S.x), S.x, S().x, type(S.x.__class__)
# <type '_ctypes.CFieldType'> <_ctypes._Field object at 0x00891E58> 0 <class '_ctypes._CField'>

print S.x.__get__(S())
print S.__dict__['x'].__get__(S())

class S2(Structure):
    _fields_ = [('spam', ctypes.c_int)]


print S2.spam
print S2.__dict__['spam']

# """int"""
#
