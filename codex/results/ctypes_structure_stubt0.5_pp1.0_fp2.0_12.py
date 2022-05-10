import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p

s = S()
s.x = ctypes.c_char_p(b"foo")
s.y = ctypes.c_char_p(b"bar")

print(s.x.value)
print(s.y.value)
</code>
This prints:
<code>foo
bar
</code>

