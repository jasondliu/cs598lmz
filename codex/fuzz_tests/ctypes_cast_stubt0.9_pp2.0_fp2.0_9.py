import ctypes
ctypes.cast(ctypes.pointer(-1), ctypes.c_char_p)
#
# ctypes.FormatError: exception formatting: ValueError('invalid \xff\xfc\xff\xfd
</code>
So this is not explicitly forbidden, but it seems you'll need to verify that your <code>pointer</code> is indeed the one you expect before doing this.

