import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# ctypes.c_char.from_address(id(libc)) is b'#'

print(type(ctypes.c_char.from_address(id(libc))))  # &lt;class 'bytes'&gt;
print(type(id(libc)))  # &lt;class 'int'&gt;
print(type(ctypes.c_char.from_address(id(libc))[0]))  # &lt;class 'int'&gt;
</code>

