import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # CField is a descriptor
print(type(S.x))
print(S.x)

def f(x):
    print("f:", x.x)

f(S(x=42))
S.x.__set__(S(x=42), 100)
print(S(x=42).x)
