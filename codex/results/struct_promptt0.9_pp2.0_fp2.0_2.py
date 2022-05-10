import _struct
# Test _struct.Struct
St = _struct.Struct("@10L")

print St.format
print St.size
print St.pack("spam", 1, 2, 3, 4)
#print St.unpack("spam", 1, 2, 3, 4)

# Test _struct.error
try:
    _struct.pack("@i")
except _struct.error, exc:
    print exc

try:
    _struct.unpack("@i")
except _struct.error, exc:
    print exc

# Test _struct.calcsize
print _struct.calcsize("@10L")

# Test packed values (compare with binascii.hexlify())
print _struct.pack("@b2B3hi", -1, -2, -3, 255, 256, 32767, 32768, 65535)

# Test pack/unpack with large buffers (for 64-bit version)
# XXX Would be nice if we could get unpackarray() back ...
a1 = _struct.pack("@8L4L4L2L4L4L4
