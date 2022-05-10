import _struct
# Test _struct.Struct.pack_into
import binascii

s = _struct.Struct('bxxxc')
bytes = buffer('a' * s.size)
s.pack_into(bytes, 0, *(1,), 'd')
print bytes
print binascii.b2a_hex(bytes)

# Test pickling
import cPickle
import random

print 'Testing pickling...',
for i in range(100):
    s = _struct.Struct("BhL")
    pickled = cPickle.dumps(s)
    new_s = cPickle.loads(pickled)
    for j in range(100):
        values = [random.randrange(0, 0xff) for i in range(3)]
        packed_value = s.pack(*values)
        unpacked = new_s.unpack(packed_value)
        if unpacked != values:
            print 'Wrong unpacked value.  Started with', values
            print 'Packed as', s.pack(*values)
            print 'Unpacked as', unpacked
            break
   
