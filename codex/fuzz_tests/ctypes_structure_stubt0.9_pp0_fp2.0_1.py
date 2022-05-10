import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

print "1..2"

def test_simple():
    ctypes.create_string_buffer(10)
    S.x.offset = 0xdeadbeef

test_simple()
print "ok"
try:
    test_simple()
except ValueError:
    print "ok"
