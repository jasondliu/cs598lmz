import ctypes
ctypes.cast(ctypes.c_void_p(0x7f3a3b9e9ed0), ctypes.py_object).value
</code>
This returns the object that is stored in that address.
However, I don't know how to get the address of the object.
The only way I know is to use the <code>id</code> function:
<code>a = [1,2,3]
id(a)
</code>
But this returns an integer, not a pointer.
How can I get the address of an object in Python?


A:

You can use <code>ctypes.addressof(obj)</code> to get the address of an object.
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.addressof(obj)
4453480
</code>

