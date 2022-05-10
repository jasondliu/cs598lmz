import ctypes
# Test ctypes.CFUNCTYPE()
try:
    CFUNCTYPE = ctypes.CFUNCTYPE
except AttributeError:
    # ctypes.CFUNCTYPE() is not present on < Python 2.5
    import _ctypes
    CFUNCTYPE = _ctypes._CFuncPtr

c_int_p = ctypes.POINTER(ctypes.c_int)

GLenum = ctypes.c_uint
GLfloat = ctypes.c_float
GLclampf = ctypes.c_float
GLboolean = ctypes.c_ubyte
GLbitfield = ctypes.c_uint

GLchar = ctypes.c_char
GLbyte = ctypes.c_byte
GLubyte = ctypes.c_ubyte
GLshort = ctypes.c_short
GLushort = ctypes.c_ushort
GLint = ctypes.c_int
GLuint = ctypes.c_uint
GLclampx = ctypes.c_int

GLsizei = ctypes.c_int
