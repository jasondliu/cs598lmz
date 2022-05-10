import _struct
# Test _struct.Struct with non-native sizes
class S(Structure):
    _fields_ = [("i", c_int), ("j", c_int)]

if sys.byteorder == "little":
    s = "ii"
else:
    s = "gg"

s = _struct.Struct(s)
try:
    s.pack(S(1, 2))
except Exception:
    print("ERROR: non-native size not supported")

# Remove the global reference to S (for clean-up)
del S
# Test _struct.Struct with nested structures
class S(Structure):
    _fields_ = [("i", c_int), ("n", c_char_p)]

try:
    s = _struct.Struct("iS")
except Exception:
    print("ERROR: nested structures not supported")

# Remove the global reference to S (for clean-up)
del S
# Test _struct.Struct with nested structures
class S(Structure):
    _fields_ = [("i", c_int), ("n", c_char_p)]

try:

