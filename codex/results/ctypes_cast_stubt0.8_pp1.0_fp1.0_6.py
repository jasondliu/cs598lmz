import ctypes
ctypes.cast(self._out_ptr, ctypes.POINTER(ctypes.c_int)).contents.value = self.o_lev
</code>
I'd like to be able to do it in a single line. What's the most elegant way to do this?


A:

Try this:
<code>ctypes.cast(self._out_ptr, 
            ctypes.POINTER(ctypes.c_int)).contents.value = self.o_lev
</code>

