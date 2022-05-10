import _struct
# Test _struct.Struct
m = _struct.calcsize('l')
value, = _struct.unpack(m, _struct.pack('l', 123))
# Test _struct.error
try:
    m = _struct.calcsize('m')
except _struct.error:
    pass
