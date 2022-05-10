import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8    # Atomic type
    y = ctypes.c_char * 64  # Sequence type

foo = ctypes.c_uint8.from_buffer(S())
print

print 'foo.value =', foo.value
print 'foo.mro =', type(foo).mro()
print 'foo.base is S =', foo.base is S

foo.value = 10
print '\nAfter foo.value = 10:'
for f in 'yz':
    print "foo.{0}.value = ({0}, {0}[0]) =".format(f),
for f in 'yz':
    print "foo.{0}.raw = ({0}, {0}[0]) =".format(f),


foo = ctypes.c_uint8.from_buffer(S(), 4)
print

print 'foo.value =', foo.value

foo.value = 160 # 160 = 0xA0, 0xA0 = 10100000

print '\nAfter foo.value = 160:'
for f in 'x':
    print "
