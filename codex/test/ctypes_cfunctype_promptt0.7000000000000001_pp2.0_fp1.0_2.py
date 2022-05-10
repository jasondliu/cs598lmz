import ctypes
# Test ctypes.CFUNCTYPE( ctypes.POINTER( ctypes.c_int ), ctypes.c_int )
class C_int_p( ctypes.Structure ):
    pass

C_int_p_p = ctypes.POINTER( C_int_p )
C_int_p_p._type_ = C_int_p

C_int_p._fields_ = [ ( "value", ctypes.c_int ) ]

