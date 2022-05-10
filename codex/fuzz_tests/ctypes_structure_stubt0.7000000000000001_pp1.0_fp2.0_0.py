import ctypes

class S(ctypes.Structure):
    x = (1,2,3)

s = S()

s.x = (4,5,6) # Fails, can't assign to tuple
</code>
On the other hand, if you use <code>c_int</code> instead of <code>int</code> then the assignment will succeed:
<code>import ctypes

class S(ctypes.Structure):
    x = (ctypes.c_int(1),ctypes.c_int(2),ctypes.c_int(3))

s = S()

s.x = (ctypes.c_int(4),ctypes.c_int(5),ctypes.c_int(6)) # Succeeds
</code>

