import ctypes
ctypes.CDLL('./01_so_module.so', mode = ctypes.RTLD_GLOBAL)

from ctypes_utils.ctypes_tools import print_c_decl

x = ctypes.c_void_p
print("void *:", print_c_decl(x, 'x'))

x = ctypes.c_char_p(b'123')
print("char *:", print_c_decl(x, 'x'))

x = ctypes.c_int(123)
print("int:", print_c_decl(x, 'x'))

x = ctypes.c_uint(123)
print("unsigned int:", print_c_decl(x, 'x'))

x = ctypes.c_float(123.0)
print("float:", print_c_decl(x, 'x'))

x = ctypes.c_short(123)
print("short:", print_c_decl(x, 'x'))

x = ctypes.c_ushort(123)
print("unsigned
