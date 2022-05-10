import _struct
# Test _struct.Struct('i').pack_into
print(_struct.Struct('i').pack_into(bytearray(10), 0, 1))
print(_struct.Struct('i').pack_into(bytearray(10), 1, 1))
print(_struct.Struct('i').pack_into(bytearray(10), 2, 1))
print(_struct.Struct('i').pack_into(bytearray(10), 1, 2**32-1))
print(_struct.Struct('i').pack_into(bytearray(10), 1, -2**32))
print(_struct.Struct('i').pack_into(bytearray(10), 2, -2**32))
print(_struct.Struct('i').pack_into(bytearray(10), 2, 2**32-1))
print(_struct.Struct('i').pack_into(bytearray(10), 0, -2**32))
