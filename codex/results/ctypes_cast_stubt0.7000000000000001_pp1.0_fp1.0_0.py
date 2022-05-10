import ctypes
ctypes.cast(sock, ctypes.c_char_p).value = 0
</code>
In your case, it would be:
<code>ctypes.cast(connection, ctypes.c_char_p).value = 0
</code>

