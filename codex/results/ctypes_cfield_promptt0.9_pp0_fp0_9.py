import ctypes
# Test ctypes.CField
###
print( "\n\n>>> None == ctypes.CField( None, None, None, 0L )" )
print( None == ctypes.CField( None, None, None, 0L ) )

class CFieldDerived( ctypes.CField ):
    pass
cfields = (
    ctypes.CField( None, ctypes.c_long, None, 0L ),
    ctypes.CField( None, ctypes.c_int, None, 0L ),
    ctypes.CField( None, ctypes.c_int, None, 1L ),
    ctypes.CField( None, ctypes.c_ubyte, None, 1L ),
    ctypes.CField( None, ctypes.c_short, None, 2L ),
    ctypes.CField( None, ctypes.c_ushort, None, 2L ),
    ctypes.CField( None, ctypes.c_byte, None, 3L ),
    ctypes.CField( None, ctypes.c_byte, None, 4L ),
    ctypes.
