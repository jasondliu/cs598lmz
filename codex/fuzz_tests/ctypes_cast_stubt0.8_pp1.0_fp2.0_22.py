import ctypes
ctypes.cast(a, ctypes.c_char_p).value
</code>
which gives the error
<code>ValueError: character buffer size too short
</code>
which is strange, because <code>a</code> should be a null-terminated string.
I don't know the length of the string beforehand, hence I can't use the <code>create_string_buffer</code> method.
Any idea?

