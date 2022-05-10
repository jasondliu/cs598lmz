import _struct

def _pack_int(i, size):
    """Pack an integer into a string of the specified size."""
    s = ''
    for _ in xrange(size):
        s += chr(i & 0xff)
        i >>= 8
    return s

def _unpack_int(s):
    """Unpack an integer from a string."""
    i = 0
    for c in s:
        i = (i << 8) | ord(c)
    return i

# This is a mixin class for classes that handle data and which want to
# be able to be passed as arguments to the built-in file() function.
#
# This is implemented by defining read(), readline(), readlines(),
# write(), writelines() and close().  To make your class into a "file"
# object you will also need to define a seek() method and a tell()
# method.  You can also use the readinto() method to write to a buffer
# instead of a file.
#
# You will also need to define a __iter__() method that returns an
# iterator
