import ctypes
# Test ctypes.CFUNCTYPE
a = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_uint)
# Test ctypes.wintypes
b = ctypes.wintypes.LPARAM
# Test ctypes.c_char_p
c  = ctypes.c_char_p('Hello World'.encode(ENCODING))
# Test ctypes.c_char
d = ctypes.c_char('H'.encode(ENCODING))
# Test ctypes.c_char_p
e = ctypes.c_char_p('Hello World\00'.encode(ENCODING))
# Test ctypes.POINTER(ctypes.c_char_p)
f = ctypes.POINTER(ctypes.c_char_p)(c)
</code>
I have added the <code>b</code> <code>c</code> and <code>d</code> incase they are interesting, but the main thing I am trying to figure is how to define <code>a</code> in a SWIG interface file. 
The C function that
