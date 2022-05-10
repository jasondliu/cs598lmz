import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32()
    y = ctypes.c_int32()

s = S()
s.x = 1
s.y = 2

print s.x
print s.y
</code>
This prints:
<code>1
2
</code>
But this prints:
<code>1
1
</code>
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32()
    y = ctypes.c_int32()

s = S()

print s.x
print s.y
</code>
I am not sure why this is the case.


A:

The issue is that you are using the same object for both fields.
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32()
    y = ctypes.c_int32()

s = S()

print s.x
print s.y

print id(s.x)
print id(s.y)

