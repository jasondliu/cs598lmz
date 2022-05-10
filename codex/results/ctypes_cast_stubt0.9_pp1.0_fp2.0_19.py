import ctypes
ctypes.cast(ctypes.create_string_buffer(b'hello world'), ctypes.c_void_p)
</code>
This creates a <code>ctypes.c_buffer</code> object with type <code>ctypes.c_char *11</code>, which is a pointer type.  In C, that would lead directly to a <code>void*</code> value, and <code>cast</code> will give you the equivalent in Python.

