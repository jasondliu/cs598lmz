import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p

a = S()
a.x = "foo"
a.y = "bar"

b = S()
b.x = "baz"
b.y = "quux"

c = S()
c.x = "baz"
c.y = "quux"

