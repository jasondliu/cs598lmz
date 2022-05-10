from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('@i')
s.unpack_from(b'\x00\x00\x00\x00', 0)[0]

#st = Struct.__new__(Struct)
#st.__init__('@i')
#st.unpack_from(b'\x00\x00\x00\x00', 0)

st = Struct('@i')
st.unpack_from(b'\x00\x00\x00\x00', 0)

# this would not work
# Struct('@i').unpack_from(b'\x00\x00\x00\x00', 0)

# this would not work
# Struct('@i').unpack_from(b'\x00\x00\x00\x00', 0)[0]

# this would work
# Struct('@i').unpack_from(b'\x00\x00\x00\x00', 0)[0][0]

# this would work
# Struct('@i').unpack_from(b'\
