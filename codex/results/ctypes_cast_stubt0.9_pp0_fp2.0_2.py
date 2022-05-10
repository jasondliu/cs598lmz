import ctypes
ctypes.cast(my_string_as_int, ctypes.c_char_p).value
</code>
But if your input numbers were too large, that would fail.  Now, if you have e.g. 19, that fits in a 32-bit int, so we can use <code>ctypes.c_uint</code> and a <code>ctypes.pointer()</code> to get the address, then index into the buffer.
<code>print( ''.join( ch, for ch in ctypes.cast((ctypes.c_uint*2).from_address(19)) ) )
ö
</code>
If you had a 64-bit value, and wanted to process it as a string, you'd use a <code>ctypes.c_uint64</code>.  But if your <code>'chr'</code> values are large enough that you need 64-bit ints, something is probably invalid, but you can figure it out, and fix it if you want to.

