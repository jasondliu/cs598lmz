import ctypes
ctypes.cast(a,ctypes.c_char_p).value

# Returns b'hello world'

ctypes.cast(a,ctypes.c_char_p).value.decode('utf-8')

# Returns 'hello world'
</code>

