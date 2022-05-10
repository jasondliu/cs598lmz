import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Bad:
    pass

try:
    ctypes.CField('x', ctypes.c_int)
except TypeError, detail:
    print repr(detail)
else:
    print "should raise TypeError"

try:
    ctypes.CField(Bad(), ctypes.c_int)
except KeyError, detail:
    print repr(detail)
else:
    print "should raise KeyError"

try:
    ctypes.CField(5, ctypes.c_int, 0)
except TypeError, detail:
    print repr(detail)
else:
    print "should raise TypeError"

try:
    ctypes.CField(S.x, ctypes.c_int, 5)
except TypeError, detail:
    print repr(detail)
else:
    print "should raise TypeError"

try:
    ctypes.CField(S.x, "int", 5)
except TypeError, detail:
    print repr(detail)
else:
    print "should raise TypeError"

try:
   
