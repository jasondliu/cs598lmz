import ctypes
# Test ctypes.CField
CFIELD_SIZE = ctypes.sizeof(ctypes.CField)
CFIELD_ALIGN = ctypes.alignment(ctypes.CField)
assert CFIELD_SIZE == 8 and CFIELD_ALIGN == 8
# Test ctypes.Field
FIELD_SIZE = ctypes.sizeof(ctypes.Field)
FIELD_ALIGN = ctypes.alignment(ctypes.Field)
assert FIELD_SIZE == 24 and FIELD_ALIGN == 8
# Test ctypes.FieldWithOffset
FIELDWITHOFFSET_SIZE = ctypes.sizeof(ctypes.FieldWithOffset)
FIELDWITHOFFSET_ALIGN = ctypes.alignment(ctypes.FieldWithOffset)
assert FIELDWITHOFFSET_SIZE == 32 and FIELDWITHOFFSET_ALIGN == 8
# Test ctypes.Array
ARRAY_SIZE = ctypes.sizeof(ctypes.Array)
ARRAY_ALIGN = ctypes.alignment(ctypes.Array)
assert ARRAY_SIZE == 16 and ARRAY_ALIGN == 8
# Test ctypes.Pointer
POINTER
