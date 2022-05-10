from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
print(s.size)
print(s.pack(1))
print(s.unpack(b'\x01\x00'))

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
# 2
# b'\x01\x00'
# (1,)

# >>>
