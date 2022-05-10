import _struct
# Test _struct.Struct
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    if _struct.calcsize('c') != struct.calcsize('c'):
        raise Exception('_struct and struct use different sizeof(char)')
    if _struct.calcsize('P') != struct.calcsize('P'):
        raise Exception('_struct and struct use different sizeof(void*)')
    # Some platforms have padding at the start of the struct.
    # Detect this, and adjust the offsets used below accordingly.
    _struct_P = _struct.Struct('ccP')
    padding = _struct_P.unpack(_struct_P.pack('\0','\0',0))[0].count('\0')
    # packing None should yield a binary string of all zero bytes
    if _struct_P.pack(None,None,None) != '\0'*(_struct_P.size-padding):
        raise Exception('_struct failed to pack None')
    # NULL pointer is all zeros
    if _struct_P.pack('\0','\0',0) !=
