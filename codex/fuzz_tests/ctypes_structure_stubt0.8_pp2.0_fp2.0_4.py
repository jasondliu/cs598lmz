import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p()

def f(s):
    s.x = ctypes.c_char_p(b"abc")

s = S()
f(s)
print(s.x)
s.x = ctypes.c_char_p(b"def")
print(s.x)
</code>
Output:
<code>abc
def
</code>
The same behaviour can be observed when a <code>ctypes.c_char_p</code> object is passed as an argument to a function, which returns another <code>ctypes.c_char_p</code> object, which is then assigned back to the field. AFAICT, the trick is that the assigned value must be a <code>ctypes.c_char_p</code> object, not a string or other object, and it must be explicitly created with <code>ctypes.c_char_p(...)</code>.
The same approach can be used with any type that is an alias for <code>c_char_p</code>, such as <code>c_wchar_p</
