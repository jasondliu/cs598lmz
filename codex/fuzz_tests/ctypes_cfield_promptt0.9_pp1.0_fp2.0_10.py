import ctypes
# Test ctypes.CField() for the following types:
#
# Argument    ctypes Type          Bytes  ctypes Field(x)
#
# char        ctypes.c_byte        1     ctypes.c_int8
# short       ctypes.c_short       2     ctypes.c_int16
# int         ctypes.c_int         sizeof(int)
# long        ctypes.c_long        sizeof(long)
# long long   ctypes.c_longlong    sizeof(long long)
#
# unsigned char     ctypes.c_ubyte         1      ctypes.c_uint8
# unsigned short    ctypes.c_ushort        2      ctypes.c_uint16
# unsigned int      ctypes.c_uint          sizeof(int)
# unsigned long     ctypes.c_ulong         sizeof(long)
# unsigned long long    ctypes.c_ulonglong    sizeof(long long)

# WARNING: For cints and for clongs, the ctypes.CField() might differ
# on different platforms. For example, on 64-bit systems, clongs
#
