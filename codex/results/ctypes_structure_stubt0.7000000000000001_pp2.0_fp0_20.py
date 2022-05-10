import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
print(type(s.x))
print(type(ctypes.c_int))
</code>
Output:
<code>&lt;class '_ctypes.PyCSimpleTypeObject'&gt;
&lt;class '_ctypes.PyCSimpleTypeObject'&gt;
</code>
Why are they different?


A:

The <code>ctypes</code> framework allows you to create your own types, like this:
<code>class MyInt(ctypes.c_int):
    def __repr__(self):
        return f"MyInt({super().__repr__()})"
</code>
Now in your example, the <code>S</code> class defines an attribute <code>x</code>, which is an instance of <code>ctypes.c_int</code>. If you were to say <code>s.x = MyInt(42)</code> you'd get an instance of <code>MyInt</code>, not <code>ctypes.c_int</code>.

