import _struct
# Test _struct.Struct

# Test alignment
# XXX: This is currently broken.
# struct.calcsize() does not return the correct size for
# non-native byte orders with alignment > 1.
# See http://bugs.python.org/issue1892
# Try to fix this, and remove the following line.
try:
    _struct.Struct('=xx')
except TypeError:
    raise TestSkipped, "Non-native byte orders not supported"

# Test all combinations of native/non-native and standard/non-standard size
for prefix in ('@','=','<','>','!'):
    for size in (1,2,4,8):
        try:
            _struct.Struct(prefix+str(size))
        except TypeError:
            pass
        else:
            print prefix+str(size),

# Test packing/unpacking
def check(fmt, vals, expected):
    s = _struct.Struct(fmt)
    res = s.pack(*vals)
    if res != expected:
        raise TestFailed, '%s != %s' % (repr
