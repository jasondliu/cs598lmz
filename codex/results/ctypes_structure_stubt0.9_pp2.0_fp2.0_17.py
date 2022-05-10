import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
print s.x
print S.x
</code>
Which prints out:
<code>0
&lt;class 'ctypes.c_int'&gt;
</code>
So, in Python, it's possible to refer to the field of a structure by name.  Whereas in C, it's not possible to refer to a struct field by itself (in general, a struct field is only usable through the struct itself). This makes me think that the structure object in Python is somehow special, although I've seen code that looks very similar in C as well: http://www.winehq.org/pipermail/wine-devel/2001-August/007356.html
So, is the structure object in Python really just a C struct? If Python really is using C structs, then why can't I do this in C?  If Python isn't using C structs, what does Python use to represent the structure object instead?


A:

While you can't refer to those fields in C by themselves, you can create a function that accepts a struct as a parameter and returns a value of one
