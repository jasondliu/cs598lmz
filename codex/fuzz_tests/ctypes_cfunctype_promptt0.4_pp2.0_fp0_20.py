import ctypes
# Test ctypes.CFUNCTYPE

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# int puts(const char *s);
puts = libc.puts
puts.argtypes = ctypes.c_char_p,
puts.restype = ctypes.c_int

# int printf(const char *format, ...);
printf = libc.printf
printf.argtypes = ctypes.c_char_p,
printf.restype = ctypes.c_int

# int fprintf(FILE *stream, const char *format, ...);
fprintf = libc.fprintf
fprintf.argtypes = ctypes.c_void_p, ctypes.c_char_p,
fprintf.restype = ctypes.c_int

# int sprintf(char *str, const char *format, ...);
sprintf = libc.sprintf
sprintf.argtypes = ctypes.c_char_p, ctypes.c_char_p,
sprintf.restype = ctypes.c_int

# int snprintf(
