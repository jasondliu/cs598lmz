import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class X(ctypes.Structure):
    _fields_ = [('a', S), ('b', S)]

x = X()
print x.a
print x.b
</code>
Output:
<code>&lt;__main__.S instance at 0x1004c06c0&gt;
&lt;__main__.S instance at 0x1004c06c0&gt;
</code>
So I guess the question is, how do I make it so that <code>x.a</code> and <code>x.b</code> are different instances of <code>S</code>?
Update:
I noticed that if I do the following, I get the result I want:
<code>x.a = S()
x.b = S()
</code>
But I'd like to have the initialization be automatic.


A:

You can't do this with <code>_fields_</code> alone.  You can, however, create a subclass of <code>X</code> that overrides <code>__new
