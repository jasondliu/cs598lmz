import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    s = S()
    print (type(s.x))
    print (ctypes.CField)
    assert type(s.x) == ctypes.CField

main()
