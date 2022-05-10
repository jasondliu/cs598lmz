import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    _fields_ = [('x', ctypes.c_char_p)]

s = S(x="foo")

print s.x
</code>
This prints <code>foo</code>. If you change the line <code>x = ctypes.c_char_p</code> to <code>x = ctypes.c_char * 3</code> it still prints <code>foo</code>, because <code>c_char * 3</code> is just a shortcut for <code>c_char_p</code>. You can see this in the documentation.

