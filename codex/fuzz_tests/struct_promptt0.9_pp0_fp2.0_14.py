import _struct
# Test _struct.Struct objects read correctly.
check(_struct.Struct('<I').unpack(_struct.pack('<I', 0x12345678))[0], 0x12345678)
# The same with standard ctypes.
check(ctypes.c_uint32.from_buffer_copy(_struct.pack('<I', 0x12345678)) == 0x12345678)

# Constants with values in range 0..255 shouldn't have leading zero.
check(binascii.crc_hqx('foo', 0) == 0xD4)

# Negative integers should result in negative float.
check(math.sin(-1) == -0.8414709848078965)

# Empty list should print as []
check(str([]) == '[]')

# Empty array should print as array('', [])
check(str(array('b')) == "array('b', [])")

# Check floats
check(str(1.0/2) == '0.5')
check(str(1.0/3) == '0.3333333333333333')
check(
