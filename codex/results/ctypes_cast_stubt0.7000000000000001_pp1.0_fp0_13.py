import ctypes
ctypes.cast(b, ctypes.py_object).value = 'hello'
b[:] = 'world'
print(a,b)

# <i> is an alias of <int> as can be seen in the source code
# You can use <i> instead of <int>
# https://docs.python.org/3/library/ctypes.html#ctypes.Array

# <i> or <int>
# https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong

# <q> or <long long>
# https://docs.python.org/3/library/ctypes.html#ctypes.c_short

# <h> or <short>
# https://docs.python.org/3/library/ctypes.html#ctypes.c_ubyte

# <B> or <unsigned char>
# https://docs.python.org/3/library/ctypes.html#ctypes.c_uint

# <I> or <unsigned int>
# https://docs.python.org/3/library
