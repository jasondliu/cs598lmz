import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    x = ctypes.c_int

print S.x
print S.x
</code>
Here is the output:
<code>&lt;member 'x' of 'S' objects&gt;
&lt;member 'x' of 'S' objects&gt;
</code>
This is the same output as if you've just defined the member once.
I am aware that this is not a problem for <code>ctypes</code>, since the <code>Structures</code> are not meant to be extended in this way. It is just a curiosity.
I've used <code>ctypes</code> as an example, but I am interested in the general case.


A:

This is what happens when you do the same thing in C++:
<code>struct S {
    int x;
    int x;
};
</code>
The first definition of <code>x</code> will be used, and the second ignored.
<code>ctypes</code> is just doing what C++ does.

