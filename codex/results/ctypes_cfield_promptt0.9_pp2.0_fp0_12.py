import ctypes
# Test ctypes.CField

if __name__ == '__main__':
    ctypes.Field.__repr__(ctypes._Field_)
    ctypes.Field.__repr__(ctypes._Field(None, '_Field', "b", 0))
    ctypes.Field.__repr__(ctypes._Field(None, '_Field', "i", 0))
    ctypes.Field.__repr__(ctypes._Field(None, '_Field', "h", 0))
    ctypes.Field.__repr__(ctypes._Field(None, '_Field', "l", 0))
    ctypes.Field.__repr__(ctypes._Field(None, '_Field', "P", 0))
    ctypes.Field.__repr__(ctypes._Field(None, '_Field', "i", 0, True))
    ctypes.Field.__repr__(ctypes._Field(None, '_Field', "i", 0, False))
    ctypes.Field.__repr__(ctypes._Field(None, '_Field', "i",
