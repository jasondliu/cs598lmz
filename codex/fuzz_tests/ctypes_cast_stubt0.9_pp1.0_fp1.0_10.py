import ctypes
ctypes.cast(b'hello', ctypes.c_char_p)
</code>
<blockquote>
<p>TypeError: bytes or integer address expected instead of _io.BytesIO object</p>
</blockquote>
How can I cast file contents to character pointer?


A:

You try to pass a *FILE* object (where your file pointer is) to cast() function. It doesn't work because the function expects a pointer value such as the one you have in a buffer.
Try this instead:
<code>ctypes.cast(buffer(b'hello'), ctypes.c_char_p)</code>

