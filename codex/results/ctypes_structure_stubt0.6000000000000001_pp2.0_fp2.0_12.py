import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 3

S.__str__ = lambda self: str(self.x)

s = S()
print(s)
</code>
But if I print <code>s.x</code> I get <code>&lt;__main__.c_int_Array_3 object at 0x7f7a6a1d6e30&gt;</code>.
I don't know how to override <code>__str__</code> of <code>s.x</code>.


A:

You can use a property:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 3

    @property
    def x_repr(self):
        return str(self.x)

    def __str__(self):
        return str(self.x)

s = S()
print(s)
print(s.x)
print(s.x_repr)
</code>
Output:
<code>(0, 0, 0)
&lt;__main
