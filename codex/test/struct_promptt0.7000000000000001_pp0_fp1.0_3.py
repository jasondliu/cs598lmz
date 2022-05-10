import _struct
# Test _struct.Struct.__init__
try:
    _struct.Struct()
except TypeError:
    pass
else:
    raise Exception("shouldn't accept no args")

try:
    _struct.Struct('')
except error:
    pass
else:
    raise Exception("shouldn't accept empty string")

try:
    _struct.Struct('@')
except error:
    pass
else:
    raise Exception("shouldn't accept just the endian code")

try:
    _struct.Struct('@i')
except error:
    pass
else:
    raise Exception("shouldn't accept non-native endian code")

try:
    _struct.Struct('=i')
except error:
    pass
else:
    raise Exception("shouldn't accept non-native endian code")

s = _struct.Struct('=i')

try:
    _struct.Struct(s)
except TypeError:
    pass
else:
    raise Exception("shouldn't accept a Struct instance")

# Test _struct.Struct.format
s = _struct.Struct
