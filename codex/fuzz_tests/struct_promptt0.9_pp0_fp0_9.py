import _struct
# Test _struct.Struct.
#
# Check _struct.Struct("i")('\0\0\0\0') raises an error.
# Check _struct.Struct("i")("") raises an error.
import _struct
# This used to crash the Python interpreter.
# The compiler now uses PyNode_FREE instead of PyNode_DecRef.
for x in (0, 255, 65535, 4294967295L):
    s = struct.pack("i", x)
    y = struct.unpack("i", s)[0]
    if x != y:
        print "unpack/pack i failed:", x, y
for x in (0, 255, 65535, 4294967295L, 9007199254740992L):
    s = struct.pack("l", x)
    y = struct.unpack("l", s)[0]
    if x != y:
        print "unpack/pack l failed:", x, y
for x in (0, 255, 65535, 4294967295L):
    s = struct.pack("I", x)
    y = struct.unpack
