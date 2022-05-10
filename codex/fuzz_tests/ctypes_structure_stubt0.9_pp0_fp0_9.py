import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p.from_buffer(b'foobarbaz')

libc = ctypes.CDLL(None)

# PyErr_SetFromErrnoWithFilenameObject should use PyUnicode_AsUTF8AndSize()
# to convert a filename to UTF-8 bytes. In the test case, this should copy the
# NUL-terminator of the 'foobarbaz' C string.
libc.open()
</code>
You can run this test case on Linux and check that <code>/tmp/foobarbaz</code> is a
valid file.

