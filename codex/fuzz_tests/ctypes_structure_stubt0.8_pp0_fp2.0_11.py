import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    s = ctypes.c_char_p
    s2 = ctypes.c_wchar_p
    s3 = ctypes.c_char * 4

S_ = ctypes.c_char * 16

s = S(b'a', S_("hello"), S_("world"), S_("bye"))
s.s = "hello"
s.s2 = "world"
s.s3 = "bye"

s = S(b'a', S_("hello"), S_("world"), S_("bye"))
s.s = b"hello"
s.s2 = b"world"
s.s3 = b"bye"

s = S(b'a', S_("hello"), S_("world"), S_("bye"))
s.s = bytearray("hello")
s.s2 = bytearray("world")
s.s3 = bytearray("bye")

s = S(b'a', S_("hello"), S_("world"), S_("bye"))
s
