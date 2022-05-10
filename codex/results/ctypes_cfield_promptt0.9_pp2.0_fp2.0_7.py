import ctypes
# Test ctypes.CField
cfield=ctypes.CField()
cfield.push(Asteriks, ctypes.c_ushort)
cfield.push(Num, ctypes.c_uint8)
cfield.push(Name, ctypes.c_string)
cfield.push(Mob, ctypes.c_uint8)
cfield.push(Class, ctypes.c_uint8)
cfield.push(Race, ctypes.c_uint8)
cfield.push(Level, ctypes.c_uint8)
cfield.push(Thumb, ctypes.c_uint16)
cfield.push(Tall, ctypes.c_uint16)
cfield.push(Len, ctypes.c_uint16)
cfield.push(Hair, ctypes.c_uint16)
cfield.push(Points, ctypes.c_uint16)
cfield.push(Win, ctypes.c_uint16 )

print( cfield.sizeofPackSize( cfield.getPack() ) )

# ctypes.CField created with __sizeof
