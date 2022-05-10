import ctypes
ctypes.cast(ctypes.c_long(123), ctypes.POINTER(ctypes.c_byte))
</code>
to obtain a <code>ctypes.POINTER(ctypes.c_byte)</code> to a binary representation of the integer <code>123</code> simply doesn't work. The above code produces conversion warnings, but still fails in strange ways.
I know that if I had a <code>ctypes.c_void_p</code> pointing to a chunk of memory with a binary representation of a number, the above code would work, but I don't have that.
Update: Thanks to lvc's answer below, I used <code>ctypes.string_at</code> to obtain a raw byte array (rather than something addressable with a pointer). Therefore I changed the title of the question not to make it misleading for other users.


A:

Did you try ctypes.string_at(pointer, size), something like that should work...

