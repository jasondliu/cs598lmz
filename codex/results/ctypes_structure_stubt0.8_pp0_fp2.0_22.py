import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_void_p
    z = ctypes.c_int

s = S()
s.x = 42
s.z = 3
print(s.contents)
</code>
yields:
<code>42
</code>
The code is declaring <code>s</code> to have the type <code>S</code> and thus <code>s</code> is an instance of <code>S</code> and not a pointer to an instance of <code>S</code>. That's why <code>s.contents</code> yields <code>42</code>.
On the other hand,
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_void_p
    z = ctypes.c_int

s = ctypes.pointer(S())
s.contents.x = 42
s.contents.z = 3
print(s.contents.x)
</code>
yields:
