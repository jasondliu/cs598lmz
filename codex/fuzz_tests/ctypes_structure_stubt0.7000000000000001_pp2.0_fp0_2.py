import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 42

s_p = ctypes.pointer(s)
s_p[0] = S(123)

print(s.x)
</code>
Output:
<code>123
</code>
The code above works, but I don't understand how it works. The code is a modified version of the example in the <code>ctypes</code> documentation. I changed the <code>Structure</code> to have only one field, and then I accessed the first element of the pointer. I expected the output to be <code>42</code> because I thought the pointer was to the original <code>Structure</code> and that I was copying the value of the first field of the <code>Structure</code> pointed to by <code>s_p</code> to the first field of the <code>Structure</code> pointed to by <code>s</code>. I assumed <code>s_p</code> was pointing to <code>s</code>. But the output was <code>123</code>. What is going on here
