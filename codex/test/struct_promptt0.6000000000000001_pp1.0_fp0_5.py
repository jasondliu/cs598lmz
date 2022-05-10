import _struct
# Test _struct.Struct

St = _struct.Struct("i")

# Unpack
print("unpack:", St.unpack(St.pack(10)))

# Unpack_from
print("unpack_from:", St.unpack_from(St.pack(10) + St.pack(20), 0))

# Pack
print("pack:", St.pack(10))

# Pack_into
buffer = bytearray(St.size)
St.pack_into(buffer, 0, 10)
print("pack_into:", buffer)
