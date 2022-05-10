import ctypes

class S(ctypes.Structure):
    x = ctypes.c_wchar_p
    y = ctypes.c_wchar_p

s = S()

s.x = "test".encode("utf-8")
s.y = "test".encode("utf-8")

print(s.x)
print(s.y)
</code>
But I get 
<code>b'test'
b'test'
</code>
What am I doing wrong here?


A:

In your definition, you have
<code>class S(ctypes.Structure):
    x = ctypes.c_wchar_p
    y = ctypes.c_wchar_p

s = S()
</code>
<code>S</code> has two <code>c_wchar_p</code> members.  And <code>c_wchar_p</code> is a pointer to a single <code>wchar_t</code> element.  So you will have to allocate a <code>ctypes.c_wchar</code>-long buffer somewhere, and then allocate a
