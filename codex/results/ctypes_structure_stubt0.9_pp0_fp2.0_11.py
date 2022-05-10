import ctypes

class S(ctypes.Structure):
    x = [("foo", ctypes.c_char * 2),
         ("bar", ctypes.c_char * 3)]
    x = [("foo", ctypes.c_char * 2),
         ("bar", ctypes.c_char * 3)]

S()
</code>
The error is:
<blockquote>
<p>&lt;&lt;&lt;class '__main__.S'&gt;&gt;&gt;: field 'x' has incomplete type</p>
</blockquote>
How can I get around this?
Edit: I know why the error occurs. I have a well-defined structure. Why is Python telling me this?


A:

Python doesn't have a concept of incomplete types, so it's telling you this because its <code>ctypes</code> module uses incomplete types to simulatate a structure that has an array of another structure as one of its members. But you can't make one such incomplete structure the member of another. Which is what you're trying to do.

So, is there any way you could restructure it to use the normal, non-incomplete
