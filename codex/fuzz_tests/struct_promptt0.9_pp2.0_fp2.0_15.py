import _struct
# Test _struct.Struct() and packing/unpacking of signed integers.

def s(size):
    return _struct.Struct("i"+size)

for size in "bhilq":
    low = getattr(sys, "maxint%d" % (size[0]*8-1))
    high = getattr(sys, "maxint%d" % (size[0]*8))
    for v in -1, low-1, low, high, high+1:
        assert _struct.unpack("<"+size, s(size).pack(v))[0] == v
        assert _struct.unpack(">"+size, s(size).pack(v))[0] == v

for size in "bhilq":
    print s(size).size

s = _struct.Struct('=*ccdc').unpack
try:
    s("abcdef")
except _struct.error:
    print "OK"
else:
    print "Error"

s = _struct.Struct('=c*').pack
print s([1, 2, 3])


