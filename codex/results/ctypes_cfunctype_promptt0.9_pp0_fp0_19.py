import ctypes
# Test ctypes.CFUNCTYPE
cfn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
try:
    cfn(4)
except TypeError:
    print "TypeError"

try:
    cfn(4)
except TypeError, e:
    print "TypeError", e


print ctypes.c_int(2**64)
print (1, ) * 2
a = (1, ) * 2
print a
print repr(a[0])
print repr(a[1])

def test(x):
    print repr(x[0])
    print repr(x[1])
    print repr(x[2])
test((3, 4, 5))
