import ctypes
ctypes.cast(0xdeadbeef, ctypes.c_void_p).value
# 3735928559

ctypes.cast(0xdeadbeef, ctypes.c_char_p).value
# b'\xef\xbe\xad\xde'

ctypes.cast(0xdeadbeef, ctypes.c_wchar_p).value
# '\udead\ubeef'

ctypes.cast(0xdeadbeef, ctypes.c_char).value
# -33

ctypes.cast(0xdeadbeef, ctypes.c_wchar).value
# '\udead'

ctypes.cast(0xdeadbeef, ctypes.c_byte).value
# -33

ctypes.cast(0xdeadbeef, ctypes.c_ubyte).value
# 221

ctypes.cast(0xdeadbeef, ctypes.c_short).value
# -5585

ctypes.cast(0xdeadbeef, ctypes.c_ushort).value
# 57005


