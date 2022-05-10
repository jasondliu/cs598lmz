import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print(s.x)
print(s.y)
</code>
The output is:
<code>0
0
</code>
I would like to know why.
I thought that the memory of the object is not initialized, so it takes the value of the previous memory.
But I tried to print the address of <code>s.x</code> and <code>s.y</code>, and they are different.
<code>print(hex(id(s.x)))
print(hex(id(s.y)))
</code>
The output is:
<code>0x7f8c8c2e0f70
0x7f8c8c2e0f78
</code>
So why are the values equal to 0?


A:

Your code is fine, but <code>c_int()</code> is not a function. It's a constructor for <code>c_int</code> objects.
<code>&gt;&gt;&
