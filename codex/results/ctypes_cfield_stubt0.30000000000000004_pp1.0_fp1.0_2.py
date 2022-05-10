import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

print D.x
print D.y
print D().x
print D().y
print C.x
print C.y
print C().x
print C().y
print S.x
print S.y
print S().x
print S().y

try:
    D.x = 1
except AttributeError:
    print "AttributeError"

try:
    D().x = 1
except AttributeError:
    print "AttributeError"

try:
    C.x = 1
except AttributeError:
    print "AttributeError"

try:
    C().x = 1
except AttributeError:
    print "AttributeError"

try:
    S.x = 1
except AttributeError:
    print "AttributeError"

try:
    S().x = 1
except AttributeError:
    print "AttributeError
