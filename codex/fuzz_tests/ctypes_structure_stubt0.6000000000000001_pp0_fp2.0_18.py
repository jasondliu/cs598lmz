import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 4
s.y = 5

a = ctypes.cast(id(s), ctypes.POINTER(S))

print a.contents.x
print a.contents.y
</code>
I would like to do the same in python but with a ctypes array:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 4
s.y = 5

a = ctypes.cast(id(s), ctypes.POINTER(S))

print a.contents.x
print a.contents.y
</code>
I would like to do the same in python but with a ctypes array:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = (S*10)
