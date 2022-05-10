import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

    def __init__(self):
    # Just for sure calling the default constructor does not change anything
        print("x1", self.x)
        super(S, self).__init__()
        print("x2", self.x)

s = S()
print("x3", s.x)
</code>
I get:
<code>x1 0
x2 0
x3 -134967296
</code>
How do I initialize the <code>c_int()</code> field of structure to zero?
And second question, will the last line actually print <code>0</code>? I mean is the <code>0</code> returned by a field shared between all instances? I can’t see how the zero integer can be shared between all instances, but it is not clear to me how the constructor works.
I have Python 3.7.6 (GCC 8.3.0) on Ubuntu 18.04.


A:

The default value is set when the class is created, so you can use that to set your default value.  And
