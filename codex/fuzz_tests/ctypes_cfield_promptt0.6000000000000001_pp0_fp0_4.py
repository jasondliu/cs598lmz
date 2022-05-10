import ctypes
# Test ctypes.CField
assert(ctypes.CField._pack_ == 1)
assert(ctypes.CField._type_ == "c")
assert(ctypes.CField._length_ == 1)

# Test ctypes.CCharField
assert(ctypes.CCharField._pack_ == 1)
assert(ctypes.CCharField._type_ == "c")
assert(ctypes.CCharField._length_ == 1)

# Test ctypes.CByteField
assert(ctypes.CByteField._pack_ == 1)
assert(ctypes.CByteField._type_ == "b")
assert(ctypes.CByteField._length_ == 1)

# Test ctypes.CUnsignedByteField
assert(ctypes.CUnsignedByteField._pack_ == 1)
assert(ctypes.CUnsignedByteField._type_ == "B")
assert(ctypes.CUnsignedByteField._length_ == 1)

# Test ctypes.CShortField
assert(ctypes.CShortField._pack_ == 1)
assert(ctypes.CShortField._type_
