import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 10

s = S()
s.x = "hello"

print s.x.value
</code>
This is a bit more complicated, but it does work.

