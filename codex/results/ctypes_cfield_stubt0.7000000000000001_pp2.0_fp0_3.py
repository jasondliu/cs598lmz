import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

x = ctypes.CField(ctypes.c_int, 'x')
print x

try:
    x.x
except AttributeError, e:
    print e

try:
    x.y
except AttributeError, e:
    print e

try:
    x.z = 42
except AttributeError, e:
    print e

print type(x.__get__(None, S))
print type(x.__get__(S(42), S))
s = S()
print type(x.__set__(s, 42))

class D(S):
    pass

print type(x.__get__(D(42), D))
print type(x.__get__(D(42), S))

print ctypes.CField(ctypes.c_char_p, 'x')
print ctypes.CField(ctypes.c_char_p, 'x').__get__(None, S)

# XXX int and long
#print ctypes.CField(ctypes.c_int, 'x
