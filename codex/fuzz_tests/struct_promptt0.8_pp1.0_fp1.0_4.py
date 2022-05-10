import _struct
# Test _struct.Struct


@cpython_api([rffi.CCHARP, rffi.INTP], PyObject)
def PyString_FromStringAndSize(space, arg0, arg1):
    """Create a new string object with a size and buffer specified.
The buffer may can contain embedded null bytes.  The string will be
limited to SIZE bytes unless SIZE is -1, in which case the string is
limited by the first null byte.  If the buffer is not NULL the new
string will use it instead of allocating memory of its own.  If the
buffer is not NULL the buffer will be initialized from the string
object.  The buffer must be at least SIZE bytes long.  If SIZE is 0
the buffer must be NULL or at least 1 byte long.  The buffer may be
reallocated using PyString_Resize() and the string size adjusted
using PyString_Size().  The string object adds a null byte at the end
of the buffer to ensure strings are null terminated.  The buffer will
be released when the string object is deallocated.  The buffer must
not be deallocated while the string object is still
