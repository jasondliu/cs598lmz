import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print C().x
print C().x.__class__
print C().x.value
print C().x.value.__class__
print C().x.value == C().x.value

try:
    C().x.value = 1
except AttributeError, e:
    print e

try:
    C().x.value = 'abc'
except TypeError, e:
    print e

try:
    C().x.value = 1.5
except TypeError, e:
    print e

try:
    C().x.value = None
except TypeError, e:
    print e

try:
    C().x.value = [1, 2, 3]
except TypeError, e:
    print e

try:
    C().x.value = (1, 2, 3)
except TypeError, e:
    print e

try:
    C().x.value = {}
except TypeError, e:

