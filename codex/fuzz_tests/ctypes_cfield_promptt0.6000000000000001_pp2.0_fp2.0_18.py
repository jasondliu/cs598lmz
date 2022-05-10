import ctypes
# Test ctypes.CField
CFieldTest = ctypes.CField(ctypes.c_ubyte, 0, 2)
CFieldTest(ctypes.c_ulong(0x1))

# Test ctypes.CSizeOf
CSizeOfTest = ctypes.CSizeOf(ctypes.c_ubyte)
CSizeOfTest(ctypes.c_ulong(0x1))

# Test ctypes.CString
CStringTest = ctypes.CString(5, ctypes.c_ubyte)
CStringTest(ctypes.c_ulong(0x1))

# Test ctypes.CStringPointer
CStringPointerTest = ctypes.CStringPointer(5, ctypes.c_ubyte)
CStringPointerTest(ctypes.c_ulong(0x1))

# Test ctypes.CUnicode
CUnicodeTest = ctypes.CUnicode(5, ctypes.c_ubyte)
CUnicodeTest(ctypes.c_ulong(0x1))

# Test c
