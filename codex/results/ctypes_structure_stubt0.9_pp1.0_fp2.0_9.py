import ctypes

class S(ctypes.Structure):
    x = 0

class X(object):
    _fields_ = [("a", ctypes.c_int),
                #("b", ctypes.c_int)]
                ("b", ctypes.c_int)]

#class Array(ctypes.Array):
#    _type_ = ctypes.c_int

X._fields_ = [("a", ctypes.c_int),
              #("b", ctypes.c_int)]
              ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _pack_ = 1

class Z(ctypes.Structure):
    #pass
    _fields_ = [("a", ctypes.c_int)]
    #_pack_ = 0 # should not be ignore
    #_pack_ = 1
    #pass
