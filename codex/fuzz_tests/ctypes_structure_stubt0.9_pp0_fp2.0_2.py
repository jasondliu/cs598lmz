import ctypes

class S(ctypes.Structure):
    x = [ctypes.c_void_p] # TypeError: 'c_void_p' object cannot be interpreted as an index

r1 = id(S.x)
r2 = id(S.x[0]) # TypeError: 'c_void_p' object cannot be interpreted as an index
</code>


A:

<blockquote>
<p>I am getting a TypeError: 'c_void_p' object cannot be interpreted as an index. In my view x is a list,</p>
</blockquote>
No, it is not. It is a field descriptor.
<blockquote>
<p>and lists can be accessed by index for a member of list, Why it shows this type error?</p>
</blockquote>
It does not show that type error for accessing <code>S.x[0]</code>. It shows it for accessing <code>S.x</code> itself, because a field descriptor doesn't work like a list. It works like a descriptor. You do not access its value directly. You access it via <code>getattr</code>.
<code>r
