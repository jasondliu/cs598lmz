import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

i = S()
s = ctypes.string_at(ctypes.byref(i), ctypes.sizeof(i))
new = ctypes.cast(ctypes.c_char_p(s), ctypes.POINTER(S))
print(new.contents.x, new.contents.y)
</code>
called.py:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

i = ctypes.pointer(S())
c = ctypes.cdll.LoadLibrary(None).one
l = ctypes.c_int(-1)
c(i, l)
print(i.contents.x, i.contents.y)
</code>
output:
<code>3 4
3 4
</code>

