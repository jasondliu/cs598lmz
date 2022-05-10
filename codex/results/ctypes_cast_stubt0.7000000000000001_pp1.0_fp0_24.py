import ctypes
ctypes.cast(p, ctypes.POINTER(ctypes.c_int32))
</code>
But this seems silly. Why should I have to tell Python what the type of the newly created pointer is? I'm asking it to give me the pointer to the first element of an array of <code>int32</code>s. Shouldn't that be enough information?

