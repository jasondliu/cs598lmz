import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Array):
    pass

class C:
    pass

class M:
    pass

class DLL:
    pass

def info(t):
    print("%s:" % t)
    print("\tbases:        %-55s %s" % (t.__bases__, [x.__name__ for x in t.__bases__]))
    print("\tmodule:       %-55s %s" % (t.__module__, str(t.__module__)))
    print("\tdict:         %-55s %s" % (t.__dict__, str(list(t.__dict__.keys())[:3]) + " ..."))
    print("\tweakrefdict:  %-55s %s" % (t.__weakrefdict__, str(t.__weakrefdict__)))
    print("\tflags:        %-55s %s" % (t.__flags__, bin(t.__flags__)))
    print("\tname:         %-
