import _struct
# Test _struct.Struct and _struct.calcsize() with an endian specifier.
Struct = _struct.Struct
calcsize = _struct.calcsize
# Little-endian byte order (le) is default.
native_types = calcsize(">i") == calcsize("<i") == 4
if native_types:
    print("native type size matches 64bit environment")
if calcsize("i") == calcsize("<i"):
    print("<i has native byte order")
else:
    print("<i does NOT have native byte order")
if calcsize("i") == calcsize("=i"):
    print("=i has native byte order")
else:
    print("=i does NOT have native byte order")
if calcsize("i") == calcsize(">i"):
    print(">i has native byte order")
else:
    print(">i does NOT have native byte order")
if calcsize("i") == calcsize("!i"):
    print("!i has native byte order")
else:
    print("!i
